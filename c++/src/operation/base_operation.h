#ifndef BASE_OPERATION_H_
#define BASE_OPERATION_H_
#include "tensorrt.pb.h"
#include "macro.h"
#include <vector>
#include "net_macro.h"
#include "arg.h"
#include "NvInfer.h"
#include <map>
#include <string>

NAME_SPACE_BEGIN

using namespace nvinfer1;



#define  TENSOR_FIND(tensor,input,ret)     \
{\
    if(tensor.count(input) ==0){ \
        LOG("no %s in NetTensor",input.c_str());\
        return ret;   \
    }\
}

#define  WEIGHT_FIND(tensor,input,ret)     \
{\
    if(tensor.count(input) ==0){ \
        LOG("no %s in weightMap",input.c_str());\
        return ret;   \
    }\
}

class BaseOp{
public: 
    BaseOp(){};

    // virtual result generateOp(nvinfer1::IPluginContainer& factory,std::map<std::string,ITensor*>&NetTensor,
    //                              INetworkDefinition*network,tensorrt::OperatorDef opDef) = 0;
    virtual result generateOp(std::map<std::string,ITensor*>&NetTensor,
                                 INetworkDefinition*network,tensorrt::OperatorDef opDef) = 0;

    void getInAndOutTensorName(tensorrt::OperatorDef opDef)
    {
        inputs_.clear();
        outputs_.clear();

        for (const std::string &input_str : opDef.input()){
            inputs_.push_back(input_str);
        }

        for(const std::string &output_str:opDef.output()){
            outputs_.push_back(output_str);
        }
    }

    void info()
    {
        LOG("input:");
        for(auto &it: inputs_){
            LOG("    %s",it.c_str());
        }

        LOG("output:");
        for(auto &it:outputs_){
            LOG("    %s",it.c_str());
        }

    }

protected:
    std::vector<std::string> inputs_;
    std::vector<std::string> outputs_;
};

NAME_SPACE_END


#endif