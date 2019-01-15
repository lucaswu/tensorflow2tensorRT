#include"mace.pb.h"
#include "ksy_model.h"

using namespace mace;

int main()
{

    NetDef *net_def = new NetDef();
    net_def->ParseFromArray(tensorrt_pb,tensorrt_pb_len);

    for (auto &input_info : net_def->input_info()) {
        printf("input_info=%s\n",input_info.name().c_str());
        
    }
    for (auto &output_info : net_def->output_info()) {
        printf("input_info=%s\n",output_info.name().c_str());
    }

    for (int idx = 0; idx < net_def->op_size(); ++idx) {
        const auto &operator_def = net_def->op(idx);
        printf("------------------create operator:%s (%s)\n",operator_def.name().c_str(),operator_def.type().c_str());

        printf("********input:\n");
        for (const std::string &input_str : operator_def.input()){
            printf("%s\n",input_str.c_str());
        }

        printf("********output:\n");
        for (const std::string &input_str : operator_def.output()){
            printf("%s\n",input_str.c_str());
        }

        
    }


    for (auto &const_tensor : net_def->tensors()) {
        printf("name:%s,size(",const_tensor.name().c_str());
        for (const int d : const_tensor.dims()) {
            printf("%d ",d);
        }
        printf(")\n");
    }


}