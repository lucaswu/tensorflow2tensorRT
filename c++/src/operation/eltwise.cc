#include "eltwise.h"
#include<string.h>

NAME_SPACE_BEGIN

std::string typeToString(EltwiseType type){
    std::string str = "NONE";
    switch (type)
    {
        case SUM: str =  "SUM";     break;
        case SUB: str = "SUB";      break;
        case PROD: str = "PROD";    break;
        case DIV: str = "DIV";      break;
        case MIN: str = "MIN";      break;
        case MAX: str = "MAX";      break;
        case NEG: str = "NEG";      break;
        case ABS: str = "ABS";      break;
        case SQR_DIFF:  str = "SQR_DIFF"; break;
        case POW: str = "POW";      break;
        case EQUAL: str = "EQUAL"; break;
        default:
            break;
    }
   return str;
}
result EltwiseOp::generateOp(IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
    result ret = Ret_Success;
    CHECK_PTR(network);
    getInAndOutTensorName(opDef);
    // info();
    if(inputs_.size() == 1 ){
        ret = processOneInput(factory,NetTensor,network,opDef);
    }
    else if(inputs_.size() == 2){
        ret = processTwoInput(NetTensor,network,opDef);
    }
    else {
        return Ret_ParamterErr;
    }

    return ret;
}

result  EltwiseOp::processOneInput(IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
    auto type = static_cast<EltwiseType>(ProtoArgHelper::GetOptionalArg<OperatorDef,int>(opDef,"type",0));
    auto scalar_input = ProtoArgHelper::GetOptionalArg<OperatorDef,float>(opDef,"scalar_input",1.0f);

    auto inputName = inputs_[0];
    TENSOR_FIND(NetTensor,inputName,Ret_ParamterErr);
    auto inputTensor = NetTensor[inputName];

    auto plugin = factory.createEltWiseScalarPlugin(type,scalar_input);
    CHECK_PTR(plugin);

    auto eltwise = network->addPlugin(&inputTensor,1,*plugin);
    CHECK_PTR(eltwise);

    eltwise->setName(opDef.name().c_str());
    eltwise->getOutput(0)->setName(outputs_[0].c_str());

    NetTensor[outputs_[0]] = eltwise->getOutput(0);

    // LOG("type=%s,scalar_input=%f",typeToString(type).c_str(),scalar_input);

    return Ret_Success;
}


result EltwiseOp::processTwoInput(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
    auto type = static_cast<EltwiseType>(ProtoArgHelper::GetOptionalArg<OperatorDef,int>(opDef,"type",0));
    LOG("type=%s",typeToString(type).c_str());

    auto operation = ElementWiseOperation::kSUM;
    switch(type){
        case SUB:   operation = ElementWiseOperation::kSUB;break;
        case PROD:  operation = ElementWiseOperation::kPROD;break;
        case MAX:   operation = ElementWiseOperation::kMAX;break; 
        case MIN:   operation = ElementWiseOperation::kMIN;break; 
        case DIV:   operation = ElementWiseOperation::kDIV;break; 
        case POW:   operation = ElementWiseOperation::kPOW;break; 
        case SUM:   operation = ElementWiseOperation::kSUM;break; 
        default:
            {
                LOG("not support op(%d) in eltwise",type);
                return Ret_NoSupportErr; 
            }
    }

    auto operator_def = opDef;

    auto outputName = operator_def.output(0);

    auto inputName  = operator_def.input(0);
    TENSOR_FIND(NetTensor,inputName,Ret_ParamterErr);
    auto tensor = NetTensor[inputName];

    auto inputName1 = operator_def.input(1);
    TENSOR_FIND(NetTensor,inputName1,Ret_ParamterErr);
    auto tensor1 = NetTensor[inputName1];

    auto add = network->addElementWise(*tensor,*tensor1,operation);
    add->getOutput(0)->setName(outputName.c_str());
    add->setName(operator_def.name().c_str());
    NetTensor[outputName] = add->getOutput(0);  


    return Ret_Success;
}

NAME_SPACE_END