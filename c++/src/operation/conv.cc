#include "conv.h"
NAME_SPACE_BEGIN
result ConvOp::generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef,void*data)
{
    result ret = Ret_Success;
    LOG("into conv generateop");

    return ret;
}

NAME_SPACE_END