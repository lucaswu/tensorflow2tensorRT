#include"net.h"
#include "model.h"
#include "cast.h"
#include "eltwise.h"
#include "concat.h"
#include "conv.h"
NAME_SPACE_BEGIN

Logger gLogger;
Net::Net()
{
    LOG("into Net");
}

Net::~Net()
{

}

nvinfer1::ICudaEngine *Net::getEnginer(int height,int width,int batchSize)
{
    result ret = Ret_Success;
    tensorrt::NetDef netDef;
    bool flag = netDef.ParseFromArray((void const*)protobuf_tensorrt_pb,(int)protobuf_tensorrt_pb_len);
    if(!flag){
        LOG("ParseFromArray error!");
        return nullptr;
    }

    ret = getWeightFromFile(netDef);
    CHECK_AND_RETURN(ret,nullptr);


    nvinfer1::IBuilder *builder = createInferBuilder(gLogger);
    CHECK_PTR_AND_RETURN(builder,nullptr);

    nvinfer1::INetworkDefinition*network = builder->createNetwork();
    CHECK_PTR_AND_RETURN(builder,nullptr);

    std::map<std::string,ITensor*>NetTensor;

    ret = getInAndOutNode(netDef,network,NetTensor,height,width);
    CHECK_AND_RETURN(ret,nullptr);

    LOG("over!");
    for(auto idx = 0;idx<netDef.op_size();idx++){
        const auto &operator_def = netDef.op(idx);
        LOG("------------------create operator:%s (%s)",operator_def.name().c_str(),operator_def.type().c_str());
        auto opType = operator_def.type();
        if(opType == "Cast"){
            CastOp op;
            ret = op.generateOp(NetTensor,network,operator_def);
        }

        if(opType == "Eltwise"){
            EltwiseOp op;
            ret = op.generateOp(NetTensor,network,operator_def); 
        }

        if(opType == "Concat"){
            ConcatOp op;
            ret = op.generateOp(NetTensor,network,operator_def); 
        }

        if(opType == "Conv2D"){
            ConvOp op;
            ret = op.generateOp(NetTensor,network,operator_def,nullptr);
        }
        if(ret != Ret_Success){
            LOG("error!");
            return nullptr;
        }

    }
    return nullptr;
}

result Net::getWeightFromFile(tensorrt::NetDef netDef)
{
   result ret = Ret_Success;
   auto getTypeSize = [](const tensorrt::TensorType dt){
        switch (dt) {
            case tensorrt::DT_FLOAT:
                return sizeof(float);
            case tensorrt::DT_UINT8:
                return sizeof(uint8_t);
            case tensorrt::DT_INT32:
                return sizeof(uint32_t);
            default:
                LOG("Unsupported data type:%d",dt);
                return (size_t)(0);
        }
   };

   int64_t model_data_size = 0;
   for(auto &const_tensor:netDef.tensors()){
               model_data_size = std::max(
        model_data_size,
        static_cast<int64_t>(const_tensor.offset() +
                             const_tensor.data_size() *getTypeSize(const_tensor.data_type())));
    }

    if(model_data_size != protobuf_tensorrt_data_len){
        LOG("weight file error!");
        return Ret_ParamterErr;
    }


    for(auto &const_tensor: netDef.tensors()){
        auto name = const_tensor.name();
        
        nvinfer1::Weights wt{nvinfer1::DataType::kFLOAT, nullptr, 0};
        wt.values = protobuf_tensorrt_data + const_tensor.offset();
        wt.count = const_tensor.data_size();
        weightMap_[name] = wt;

        std::vector<int> dims;
        for(auto &in: const_tensor.dims()){
            dims.push_back(in);
        }

        KernelSizeMap_[name] = dims;

    }

}

result Net::getInAndOutNode(tensorrt::NetDef netdef,nvinfer1::INetworkDefinition *network,
      std::map<std::string,nvinfer1::ITensor*>&NetTensor,int height,int width)
{
    LOG("net input node:%d,output nodes:%d",netdef.input_info_size(),netdef.output_info_size());

    inputNodes_.clear();
    outputNodes_.clear();

    for(auto i=0;i<netdef.input_info_size();i++){
        auto input = netdef.input_info(i);
        auto dim = input.dims();

        int height_tensor = (int)(dim[1]*height);
        int width_tensor = (int)(dim[2]*width);
        int channel_tensor = (int)(dim[3]);

        auto data = network->addInput(input.name().c_str(), nvinfer1::DataType::kFLOAT, DimsCHW{channel_tensor, width_tensor, height_tensor});
        CHECK_PTR(data);
        NetTensor[input.name()] = data;

        inputNodes_.push_back(input.name());

        // LOG("name=%s,srcSize(%d,%d),size(%d,%d,%d)",input.name().c_str(),height,width,height_tensor,width_tensor,channel_tensor);
    }

    for(auto i = 0;i<netdef.output_info_size();i++){
        auto output = netdef.output_info(i);

        outputNodes_.push_back(output.name());

        // LOG("output name:%s",output.name().c_str());

    }


    


    return Ret_Success;
}
NAME_SPACE_END