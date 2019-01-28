#ifndef PLUGIN_H_
#define PLUGIN_H_
#include "macro.h"
#include "NvInfer.h"
#include "tensorrt.pb.h"
NAME_SPACE_BEGIN

using namespace nvinfer1;
class IPluginContainer
{
public:
    virtual ~IPluginContainer() = default;

    // virtual IPlugin* createSubpixelPlugin(int scale) = 0;
    // virtual IPlugin* deserializeSubpixelPlugin(const void* data, size_t size) = 0;

    // virtual IPlugin* createResizePlugin(int scale,InterpolationModel model) = 0;
    // virtual IPlugin* deserializeResizePlugin(const void* data, size_t size) = 0;

    // virtual IPlugin* createDepthWiseConvolution(std::vector<Weights> weightParameter,ActivationModel type) = 0;
    // virtual IPlugin* deserializeDepthWiseConvolution(const void* data, size_t size) = 0;

    virtual IPlugin* createCastPlugin(tensorrt::TensorType srcType,tensorrt::TensorType dstType) = 0;
    virtual IPlugin* deserializeCastPlugin(const void*data,size_t size) = 0;

    // virtual IPlugin* createEltWiseScalarPlugin(int type,float scalarValue) = 0;
    // virtual IPlugin* deserializeWiseScalarPlugin(const void*data,size_t size) = 0;

    // virtual IPlugin* createSplitPlugin(int axis,std::vector<int> output_length) = 0 ;
    // virtual IPlugin* deserializeSplitPlugin(const void*data,size_t size) = 0;

    static std::shared_ptr<IPluginContainer> create();
};

NAME_SPACE_END;
#endif