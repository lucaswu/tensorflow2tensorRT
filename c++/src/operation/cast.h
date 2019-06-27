#ifndef CAST_H_
#define CAST_H_
#include "base_operation.h"
NAME_SPACE_BEGIN
class CastOp:public BaseOp{
public:
    CastOp(){};
    result generateOp(IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
    {
        CHECK_PTR(network);
        getInAndOutTensorName(opDef);

        info();

        auto srcType = static_cast<tensorrt::TensorType>(ProtoArgHelper::GetOptionalArg<OperatorDef,int>(opDef,"T",0));
        auto dstType = static_cast<tensorrt::TensorType>(opDef.output_type(0));
        // LOG("srcType=%d,dstType=%d",srcType,dstType );


        auto inputName = inputs_[0];
        TENSOR_FIND(NetTensor,inputName,Ret_ParamterErr);
        auto inputTensor = NetTensor[inputName];
        // LOG("srcType=%d,dstType=%d,intput name=%s",srcType,dstType ,inputName.c_str());

        auto plugin = factory.createCastPlugin(srcType,dstType);
        auto castPlugin = network->addPlugin(&inputTensor,1,*plugin);
        CHECK_PTR(castPlugin);
        castPlugin->setName(opDef.name().c_str());
        castPlugin->getOutput(0)->setName(outputs_[0].c_str());
        NetTensor[outputs_[0]] = castPlugin->getOutput(0);


        return Ret_Success;
    }
};
NAME_SPACE_END

#endif