#include <assert.h>
#include "internal_plugin.h"
#include <string>
#include "gpu_kernel.h"

NAME_SPACE_BEGIN
class CastPlugin:public IPluginExt
{
public:
    CastPlugin(tensorrt::TensorType srcType,tensorrt::TensorType dstType)
    :srcType_(srcType)
    ,dstType_(dstType)
    ,length_(0)
    {
        // KSY_LOG("CastLayer");
    }

    CastPlugin(const void* data, size_t size)
    {
       
    }

    ~CastPlugin()
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
        LOG("cast enqueue");
        result ret = Ret_Success;
        if(srcType_ == 2 && dstType_ == 1){
            uint8_t *pSrc =(uint8_t*)inputs[0];
            float* pDst = (float*)outputs[0]; 
            ret = cast_gpu(pSrc,pDst,length_);
            if(ret != Ret_Success){
                return -1;
            }
        }
        else if(srcType_ == 1 && dstType_ == 2){
            uint8_t *pDst =(uint8_t*)outputs[0];
            float* pSrc = (float*)inputs[0];
            ret = cast_gpu(pSrc,pDst,length_); 
            if(ret != Ret_Success){
                return -1;
            }
        }
        else{
            return -1;
        }
        return 0;
    }
    size_t getSerializationSize() override
    {   
        return 0;
    }
    
    void serialize(void* buffer) override
    {
        assert(buffer != nullptr);

       
    }
    

private:
    tensorrt::TensorType srcType_;
    tensorrt::TensorType dstType_;
    int length_;
};

IPlugin* PluginContainer::createCastPlugin(tensorrt::TensorType srcType,tensorrt::TensorType dstType)
{
    std::lock_guard<std::mutex> lock(lock_);
    plugins_.push_back(new CastPlugin(srcType,dstType));
    return plugins_.back();
}
IPlugin* PluginContainer::deserializeCastPlugin(const void*data,size_t size) 
{
    std::lock_guard<std::mutex> lock(lock_);
    plugins_.push_back(new CastPlugin(data,size));
    return plugins_.back();
}
NAME_SPACE_END
