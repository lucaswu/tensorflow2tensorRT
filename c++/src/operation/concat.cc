#include "concat.h"

NAME_SPACE_BEGIN

result ConcatOp::generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
    auto ret = Ret_Success;
    CHECK_PTR(network);
    getInAndOutTensorName(opDef);
    // info();
    LOG("into concat ");
    return ret;
}
NAME_SPACE_END