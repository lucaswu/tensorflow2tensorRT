#ifndef GPU_KERNEL_H
#define GPU_KERNEL_H
#include <cuda.h>
#include "macro.h"
NAME_SPACE_BEGIN

#define GWS(a,b)  (((a)+(b)-1)/(b))

template<typename T1, typename T2>
result cast_gpu(T1 *pSrc,T2*pDst,int length);


NAME_SPACE_END
#endif