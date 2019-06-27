#include "activation.h"

NAME_SPACE_BEGIN

result ActivationOp::generateOp(std::map<std::string,ITensor*>&NetTensor,
            INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
    CHECK_PTR(network);
    getInAndOutTensorName(opDef);

    LOG("into activation op");
    info();

    auto operator_def = opDef;
    TypeActivation type = static_cast<TypeActivation>(ProtoArgHelper::GetOptionalArg<OperatorDef,int>(operator_def,"activation",0));

    auto type_tensorRT = ActivationType::kRELU;
    switch(type){
        case RELU:      type_tensorRT = ActivationType::kRELU; break;
        case TANH:      type_tensorRT = ActivationType::kTANH; break;
        case SIGMOID:   type_tensorRT = ActivationType::kSIGMOID; break;
        default:
            {
                LOG("not suport type(%d) activation operation now",type);
                return Ret_NoSupportErr;
            }
    }
    if(inputs_.size() != 1 || outputs_.size() != 1){
        LOG("input/output size (%d/%d) error ",inputs_.size(),outputs_.size());
        return Ret_ParamterErr;
    }
    auto inputName  = inputs_[0];
    auto outputName = outputs_[0];

    TENSOR_FIND(NetTensor,inputName,Ret_ParamterErr);
    auto inputTensor = NetTensor[inputName];

    auto plugin = network->addActivation(*inputTensor, type_tensorRT);
    
    CHECK_PTR(plugin);
    plugin->setName(operator_def.name().c_str());
    plugin->getOutput(0)->setName(outputs_[0].c_str());

    NetTensor[outputs_[0]] = plugin->getOutput(0);

    return Ret_Success;
}

NAME_SPACE_END