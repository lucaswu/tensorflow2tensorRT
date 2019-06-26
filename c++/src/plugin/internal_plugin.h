#ifndef INTERNAL_PLUGIN_H_
#define INTERNAL_PLUGIN_H_
#include "plugin.h"
#include "tensorrt.pb.h"
#include "macro.h"
#include <mutex>

NAME_SPACE_BEGIN

class PluginContainer: public IPluginContainer
{
public:
    PluginContainer(){}

    ~PluginContainer(){};
    // IPlugin* createSubpixelPlugin(int scale) override;
    // IPlugin* deserializeSubpixelPlugin(const void* data, size_t size) override;
    
    // IPlugin* createResizePlugin(int scale,InterpolationModel model) override;
    // IPlugin* deserializeResizePlugin(const void* data, size_t size) override;

    // IPlugin* createDepthWiseConvolution(std::vector<Weights> weightParameter,ActivationModel type) override;
    // IPlugin* deserializeDepthWiseConvolution(const void* data, size_t size) override;

    IPlugin* createCastPlugin(tensorrt::TensorType srcType,tensorrt::TensorType dstType) override;
    IPlugin* deserializeCastPlugin(const void*data,size_t size) override;

    IPlugin* createEltWiseScalarPlugin(int type,float scalarValue) override;
    IPlugin* deserializeWiseScalarPlugin(const void*data,size_t size) override;

    // IPlugin* createSplitPlugin(int axis,std::vector<int> output_length) override ;
    // IPlugin* deserializeSplitPlugin(const void*data,size_t size) override;


private:
    std::vector<IPlugin*> plugins_;
    std::mutex            lock_;
};


NAME_SPACE_END
#endif