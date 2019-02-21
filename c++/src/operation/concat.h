#ifndef CONCAT_H_
#define CONCAT_H_
#include "base_operation.h"
NAME_SPACE_BEGIN
class ConcatOp:public BaseOp{
public:
    ConcatOp(){};
    result generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef) ;

};

NAME_SPACE_END

#endif

