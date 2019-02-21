#ifndef CONV_H_
#define CONV_H_
#include "base_operation.h"
NAME_SPACE_BEGIN
class ConvOp:public BaseOp{
public:
    ConvOp(){};
    result generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef,void*data) ;

};

NAME_SPACE_END

#endif