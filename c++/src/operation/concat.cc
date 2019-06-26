#include "concat.h"

NAME_SPACE_BEGIN

result ConcatOp::generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef)
{
    auto ret = Ret_Success;
    CHECK_PTR(network);
    getInAndOutTensorName(opDef);
    
    std::vector<ITensor*> concate;
    for(auto &name:opDef.input()){
        TENSOR_FIND(NetTensor,name,Ret_ParamterErr);
        auto tensor = NetTensor[name];
        concate.push_back(tensor);
    }   
            
    auto outputName = opDef.output(0);

    auto concat = network->addConcatenation(concate.data(),concate.size());
    CHECK_PTR(concat);
    concat->setName(opDef.name().c_str());
    concat->getOutput(0)->setName(outputName.c_str());
    NetTensor[outputName] = concat->getOutput(0);  

    return ret;
}
NAME_SPACE_END