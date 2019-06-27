
#ifndef ELTWISE_H_
#define ELTWISE_H_
#include "base_operation.h"
NAME_SPACE_BEGIN
class EltwiseOp:public BaseOp{
public:
    EltwiseOp(){};
    result generateOp(IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef) ;
    void setWeightTensorMap(std::map<std::string, Weights> weightMap);
private:
    std::map<std::string, Weights> weightMap_;
    
    result processOneInput(IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef);
    result processTwoInput(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef);
};
NAME_SPACE_END


#endif