#include "eltwise.h"
NAME_SPACE_BEGIN
result EltwiseOp::generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
    result ret = Ret_Success;
    LOG("into eletwise generateop");
    CHECK_PTR(network);
    getInAndOutTensorName(opDef);
    info();

    if(inputs_.size() == 1 ){
        ret = processOneInput(NetTensor,network,opDef);
    }
    else if(inputs_.size() == 2){
        ret = processTwoInput(NetTensor,network,opDef);
    }
    else {
        return Ret_ParamterErr;
    }

    return ret;
}

result  EltwiseOp::processOneInput(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
    auto type = static_cast<tensorrt::TensorType>(ProtoArgHelper::GetOptionalArg<OperatorDef,int>(opDef,"type",0));
    auto scalar_input = ProtoArgHelper::GetOptionalArg<OperatorDef,float>(opDef,"scalar_input",1.0f);

    // auto inputName = inputs_[0];
    // TENSOR_FIND(NetTensor,inputName,Ret_ParamterErr);
    // auto inputTensor = NetTensor[inputName];



    LOG("type=%d,scalar_input=%f",type,scalar_input);

    return Ret_Success;
}


result EltwiseOp::processTwoInput(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{

}

NAME_SPACE_END