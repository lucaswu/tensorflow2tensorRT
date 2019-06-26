
#ifndef ELTWISE_H_
#define ELTWISE_H_
#include "base_operation.h"
NAME_SPACE_BEGIN
class EltwiseOp:public BaseOp{
public:
    EltwiseOp(){};
    result generateOp(IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef) ;
private:
    result processOneInput(IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef);
    result processTwoInput(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef);
};
NAME_SPACE_END


#endif