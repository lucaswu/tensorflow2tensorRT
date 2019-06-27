
#ifndef ACTIVATION_H_
#define ACTIVATION_H_
#include "base_operation.h"
NAME_SPACE_BEGIN

class ActivationOp:public  BaseOp{
public:
    result generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef);
};
NAME_SPACE_END
#endif