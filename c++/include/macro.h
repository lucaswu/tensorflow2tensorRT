#ifndef MACRO_H_
#define MACRO_H_

#include "log.h"
#include "err.h"

#define LOG(format,...) logPrintf(__FILE__,__func__,__LINE__,format,##__VA_ARGS__ )


#endif