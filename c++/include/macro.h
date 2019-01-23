#ifndef MACRO_H_
#define MACRO_H_

#include "log.h"
#include "err.h"

#define LOG(format,...) logPrintf(__FILE__,__func__,__LINE__,format,##__VA_ARGS__ )


#define NAME_SPACE_BEGIN namespace parser{
#define NAME_SPACE_END }


#define CHECK(ret) \
{ \
    do{\
        if(ret!=Ret_Success){ \
            return ret;\
        }\
    }while(0);\
}    

#define CHECK_PTR(ret) \
{ \
    do{\
        if(ret==nullptr){\
            LOG("error");\
            return Ret_MemAllocErr;\
        } \
    }while(0);\
}  


#define CHECK_AND_RETURN(ret ,result)\
{ \
    do{\
        if(ret!=Ret_Success){\
            LOG("error");\
            return result;\
        }\
    }while(0); \
}

#define CHECK_PTR_AND_RETURN(ret ,result)\
{ \
    do{ \
        if(ret==nullptr){\
            LOG("nullptr ptr");\
            return result;\
        }\
    }while(0);\
}

typedef int result;

#endif