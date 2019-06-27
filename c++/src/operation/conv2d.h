#ifndef CONV_H_
#define CONV_H_
#include "base_operation.h"
NAME_SPACE_BEGIN
class ConvOp:public BaseOp{
public:
    ConvOp(){};
    result generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef) ;
    void setWeightTensorMap(std::map<std::string, Weights> weightMap);
    void setkernelSizeMap(std::map<std::string,std::vector<int>> KernelSizeMap);
private:
    std::map<std::string, Weights> weightMap_;
    std::map<std::string,std::vector<int>> KernelSizeMap_;
};

NAME_SPACE_END

#endif