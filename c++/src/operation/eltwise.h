#include "base_operation.h"
NAME_SPACE_BEGIN
class EltwiseOp:public BaseOp{
public:
    EltwiseOp(){};
    result generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef) override;
private:
    result processOneInput(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef);
    result processTwoInput(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef);
};

NAME_SPACE_END