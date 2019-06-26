#include "internal_plugin.h"

NAME_SPACE_BEGIN

std::shared_ptr<IPluginContainer> IPluginContainer::create()
{
    return std::make_shared<PluginContainer>();
}


PluginFactor::PluginFactor(IPluginContainer&container):
container_(container)
{

}

IPlugin* PluginFactor::createPlugin(const char* layerName, const void* serialData, size_t serialLength)
{
    
    size_t bytes_read = 0;
    auto ptr = (const char*)serialData;
    auto pluginType = (PluginType)*(int*)ptr;
    bytes_read += sizeof(int32_t);
    ptr += bytes_read;
    IPlugin* plugin = nullptr;

    switch(pluginType){
        // case PluginType::kResize:
        //     // KSY_LOG("resize");
        //     plugin = container_.deserializeResizePlugin(ptr, serialLength - bytes_read);
        //     break;
        // case PluginType::kDepthWise:
        //     // KSY_LOG("deptwise");
        //     plugin = container_.deserializeDepthWiseConvolution(ptr, serialLength - bytes_read);
        //     break;
        // case PluginType::kSubpixel:
        //     // KSY_LOG("subpixel");
        //     plugin = container_.deserializeSubpixelPlugin(ptr, serialLength - bytes_read);
        //     break;
        case PluginType::kCast:
            plugin = container_.deserializeCastPlugin(ptr,serialLength - bytes_read);
            break;
        case PluginType::kEltwiseScalar:
            plugin = container_.deserializeWiseScalarPlugin(ptr,serialLength-bytes_read);
            break;
    }
    return plugin;

}

NAME_SPACE_END