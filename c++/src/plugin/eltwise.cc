#include <assert.h>
#include "internal_plugin.h"
#include <string>
#include "gpu_kernel.h"
#include "serialize.h"

NAME_SPACE_BEGIN
class EltWiseLayer:public IPluginExt
{
public:
    EltWiseLayer(int type,float scalar_value)
    :type_(type)
    ,length_(0)
    {

    }

    EltWiseLayer(const void* data, size_t size)
    {
        deserialize_value(&data,&size,&type_);
        deserialize_value(&data,&size,&length_);
        deserialize_value(&data,&size,&scalar_value_);
    }

    ~EltWiseLayer()
    {

    }

    int getNbOutputs() const override
    {
        return 1;
    }

    Dims getOutputDimensions(int index, const Dims* inputs, int nbInputDims) override
    {
        assert(index==0);
        assert(nbInputDims==1);   


        length_ = 1;
        for(auto i=0;i<inputs[0].nbDims;i++){
            length_ *= inputs[0].d[i];
        }
        return inputs[0];

    }
    bool supportsFormat(DataType type, PluginFormat format) const override
    {
        return true;
    }
    void configureWithFormat(const Dims* inputDims, int nbInputs, const Dims* outputDims, int nbOutputs, DataType type, PluginFormat format, int maxBatchSize) override
    {
        
      
    }
    int initialize() override
    {
    
        return 0;
    }
    void terminate() override
    {

    }
    size_t getWorkspaceSize(int maxBatchSize) const override
    {
        return 0;
    }
    int enqueue(int batchSize, const void*const * inputs, void** outputs, void* workspace, cudaStream_t stream) override
    {
        LOG("eltwisescalar enqueue");
        float *pSrc = (float*)inputs[0]; 
        float *pDst = (float*)outputs[0]; 

        auto ret = eltwiseScalar_gpu(pSrc,pDst,length_,scalar_value_,type_);
        if(ret != Ret_Success){
            return -1;
        }

        return 0;
        
    }
    size_t getSerializationSize() override
    {   
        return serialized_size((int)PluginFactor::PluginType::kEltwiseScalar)+
               serialized_size((int)type_) +
               serialized_size((int)length_)+
               serialized_size((float)scalar_value_);
    }
    
    void serialize(void* buffer) override
    {
        assert(buffer != nullptr);

        assert(buffer != nullptr);
        serialize_value(&buffer,(int)PluginFactor::PluginType::kEltwiseScalar);
        serialize_value(&buffer,(int)type_);
        serialize_value(&buffer,(int)length_);
        serialize_value(&buffer,(float)scalar_value_);

    }
    
private:
    int type_;
    int length_;
    float scalar_value_;
};



IPlugin* PluginContainer::createEltWiseScalarPlugin(int type,float scalarValue)
{
    std::lock_guard<std::mutex> lock(lock_);
    plugins_.push_back(new EltWiseLayer(type,scalarValue));
    return plugins_.back();
}
IPlugin* PluginContainer::deserializeWiseScalarPlugin(const void*data,size_t size) 
{
    std::lock_guard<std::mutex> lock(lock_);
    plugins_.push_back(new EltWiseLayer(data,size));
    return plugins_.back();
}
NAME_SPACE_END
