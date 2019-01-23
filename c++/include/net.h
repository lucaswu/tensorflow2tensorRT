    #ifndef NET_H_
#define NET_H_
#include "macro.h"
#include "tensorrt.pb.h"
#include "NvInfer.h"
#include <map>
#include <string>

NAME_SPACE_BEGIN

using namespace nvinfer1;
class Logger : public ILogger
{
public:
    void log(ILogger::Severity severity, const char* msg) override
    {
        // suppress info-level messages
        if (severity == Severity::kINFO) return;

        switch (severity)
        {
            case Severity::kINTERNAL_ERROR: 
                printf("INTERNAL_ERROR: \n"); break;
            case Severity::kERROR: 
                printf("ERROR: \n"); break;
            case Severity::kWARNING: 
                printf("WARNING: \n"); break;
            case Severity::kINFO: 
                printf("INFO: \n"); break;
            default: 
                printf("UNKNOWN: "); break;
        }
        printf("%s\n",msg);
    }
};

struct Profiler : public IProfiler
{
	typedef std::pair<std::string, float> Record;
	std::vector<Record> mProfile;

	virtual void reportLayerTime(const char* layerName, float ms)
	{
		auto record = std::find_if(mProfile.begin(), mProfile.end(), [&](const Record& r){ return r.first == layerName; });
		if (record == mProfile.end())
			mProfile.push_back(std::make_pair(layerName, ms));
		else
			record->second += ms;
	}

	void printLayerTimes()
	{
		float totalTime = 0;
		for (size_t i = 0; i < mProfile.size(); i++)
		{
			printf("%-40.40s %4.3fms\n", mProfile[i].first.c_str(), mProfile[i].second *1e-3);
			totalTime += mProfile[i].second;
		}
		printf("Time over all layers: %4.3f\n", totalTime*1e-3);
	}

} ;


class Net
{
public:
    Net();
    ~Net();
    nvinfer1::ICudaEngine *getEnginer(int height,int width,int batchSize);
private:
    result getWeightFromFile(tensorrt::NetDef netDef);
    result getInAndOutNode(tensorrt::NetDef netdef,nvinfer1::INetworkDefinition *network,
      std::map<std::string,nvinfer1::ITensor*>NetTensor,int height,int width);


private:      
    std::map<std::string,nvinfer1::Weights> weightMap_;
    std::map<std::string,std::vector<int>>KernelSizeMap_;
    std::vector<std::string> inputNodes_;
    std::vector<std::string> outputNodes_;
    
    

};
NAME_SPACE_END


#endif