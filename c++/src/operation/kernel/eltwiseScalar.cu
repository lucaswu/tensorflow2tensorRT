#include "gpu_kernel.h"

NAME_SPACE_BEGIN
template<typename T1,typename T2>
__global__ void eltwiseScalarKernel_gpu(T1*pSrc,T2*pDst,int length,float scalar_value,int type )
{
    int idx = blockIdx.x*blockDim.x + threadIdx.x;
    if(idx < length){
        T1 data = pSrc[idx];
        switch(type){
            case 0: pDst[idx] = data + scalar_value; break;
            case 1: pDst[idx] = data - scalar_value; break;
            case 2: pDst[idx] = data * scalar_value; break;
            case 3: pDst[idx] = data / scalar_value; break;
            case 4: pDst[idx] = fmin(data,scalar_value);break;
            case 5: pDst[idx] = fmax(data,scalar_value);break;
            case 7: pDst[idx] = fabs(data);break;
            case 8: 
                {   
                    T1 diff = data - scalar_value;
                    pDst[idx] = diff*diff;break;
                }    
            case 9: pDst[idx] = pow(data,scalar_value);break;
        }
         
    }
}

template<typename T1, typename T2>
result eltwiseScalar_gpu(T1* pSrc,T2* pDst,int length,float scalar_value,int type)
{
    auto ret = Ret_Success;

    CHECK_PTR(pSrc);
    CHECK_PTR(pDst);

    dim3 threadsPerBlock(512);
    dim3 blockSPerGrid(GWS(length, threadsPerBlock.x));

    switch(type){
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 8:
        case 7:
        case 9:break;
        default:
            return Ret_NoSupportErr;
    };

    eltwiseScalarKernel_gpu<<<blockSPerGrid,threadsPerBlock>>>(pSrc,pDst,length,scalar_value,type);
    return ret;
}


template result eltwiseScalar_gpu(float* ,float* ,int ,float ,int );


NAME_SPACE_END