#ifndef NET_H_
#define NET_H_
#include "macro.h"
#include "tensorrt.pb.h"
NAME_SPACE_BEGIN

class Net
{
public:
    Net();
    ~Net();
private:
    parserResult getWeightFromFile(tensorrt::NetDef netDef);

};
NAME_SPACE_END


#endif