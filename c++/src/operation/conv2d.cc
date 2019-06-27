#include "conv2d.h"
NAME_SPACE_BEGIN
void ConvOp::setWeightTensorMap(std::map<std::string, Weights> weightMap)
{
    weightMap_ = weightMap;
}

void ConvOp::setkernelSizeMap(std::map<std::string,std::vector<int>> KernelSizeMap)
{
    KernelSizeMap_ = KernelSizeMap;
}
result ConvOp::generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
  
    
    result ret = Ret_Success;
    getInAndOutTensorName(opDef);

    info();
    
    std::vector<int> strides(ProtoArgHelper::GetRepeatedArgs<OperatorDef,int>(opDef,"strides"));
    
    Padding paddingType = static_cast<Padding>(ProtoArgHelper::GetOptionalArg<OperatorDef,int>(opDef,"padding",static_cast<int>(SAME)));

    std::vector<int> paddings(ProtoArgHelper::GetRepeatedArgs<OperatorDef,int>(opDef,"padding_values"));
    std::vector<int> dilations(ProtoArgHelper::GetRepeatedArgs<OperatorDef,int>(opDef,"dilations",{1,1}));

    TypeActivation type = static_cast<TypeActivation>(ProtoArgHelper::GetOptionalArg<OperatorDef,int>(opDef,"activation",0));

    if(opDef.input_size()<=2){
        LOG("input number is error(%s),need  3 inputs",opDef.input_size());
        return Ret_ParamterErr;
    }

    auto inputName = opDef.input(0);
    auto outputName = opDef.output(0);

    TENSOR_FIND(NetTensor,inputName,Ret_ParamterErr);
    auto inputTensor = NetTensor[inputName];

            
    if(opDef.input_size() ==2 ){
        auto weightName = opDef.input(1);
        WEIGHT_FIND(weightMap_,weightName,Ret_ParamterErr);
        LOG("Not support now");
        return Ret_NoSupportErr;
    }
    else if(opDef.input_size() == 3){
        auto weightName = opDef.input(1);
        auto biasName = opDef.input(2);
               
        WEIGHT_FIND(weightMap_,weightName,Ret_ParamterErr);
        WEIGHT_FIND(weightMap_,biasName,Ret_ParamterErr);
        auto weightTensor = weightMap_[weightName];
        auto biasTensor = weightMap_[biasName];
 
        auto kernelSize = KernelSizeMap_[weightName];
        auto conv = network->addConvolution(*inputTensor,kernelSize[0],DimsHW{kernelSize[2],kernelSize[3]},weightTensor,biasTensor);
        CHECK_PTR(conv);
        conv->setStride(DimsHW{strides[0], strides[1]});
        conv->setPadding(DimsHW{kernelSize[2]>>1,kernelSize[3]>>1});

        if(type == RELU){
            auto relu = network->addActivation(*conv->getOutput(0), ActivationType::kRELU);
            relu->setName(opDef.name().c_str());
            relu->getOutput(0)->setName(outputName.c_str());
            NetTensor[outputName] = relu->getOutput(0);  
        }
        else if( type == NOOP){
            NetTensor[outputName] = conv->getOutput(0);  
        } 
        else{
            LOG("Not support now");
            return Ret_NoSupportErr;
        }  
                           
    }

    
    return Ret_Success;
}

NAME_SPACE_END