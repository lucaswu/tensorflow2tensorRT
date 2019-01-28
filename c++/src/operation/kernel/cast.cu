#include "gpu_kernel.h"
NAME_SPACE_BEGIN

template<typename T1,typename T2>
__global__ void castkernel_gpu(T1 *pSrc,T2*pDst,int length)
{
    int idx = blockIdx.x*blockDim.x + threadIdx.x;
    if(idx < length){
        pDst[idx] = pSrc[idx];
    }
}

template<typename T1, typename T2>
result cast_gpu(T1 *pSrc,T2*pDst,int length)
{
    result ret = Ret_Success;

    // CHECK_PTR(pSrc);
    // CHECK_PTR(pDst);

    dim3 threadsPerBlock(512);
    dim3 blockSPerGrid(GWS(length, threadsPerBlock.x));

    castkernel_gpu<<<blockSPerGrid,threadsPerBlock>>>(pSrc,pDst,length);
    return ret;
}

template result cast_gpu(unsigned char*,float* ,int);
template result cast_gpu(float*,unsigned char*, int);

NAME_SPACE_END