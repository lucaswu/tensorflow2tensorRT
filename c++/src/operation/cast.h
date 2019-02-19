#include "base_operation.h"
NAME_SPACE_BEGIN
class CastOp:public BaseOp{
public:
    CastOp(){};
    // result generateOp(nvinfer1::IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
    //                              INetworkDefinition*network,tensorrt::OperatorDef opDef)
    // {
    //     CHECK_PTR(network);
    //     getInAndOutNode(opDef);
    // }

    result generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
    {
        LOG("into generateOp");
        CHECK_PTR(network);
        getInAndOutTensorName(opDef);

        info();

        auto srcType = static_cast<tensorrt::TensorType>(ProtoArgHelper::GetOptionalArg<OperatorDef,int>(opDef,"T",0));
        auto dstType = static_cast<tensorrt::TensorType>(opDef.output_type(0));
        LOG("srcType=%d,dstType=%d",srcType,dstType );


        auto inputName = inputs_[0];
        TENSOR_FIND(NetTensor,inputName,Ret_ParamterErr);
        auto inputTensor = NetTensor[inputName];
        LOG("srcType=%d,dstType=%d,intput name=%s",srcType,dstType ,inputName.c_str());

        return Ret_Success;
    }
};
NAME_SPACE_END