#ifndef ERR_H_
#define ERR_H_

#define CONVERTCODE(ret)                (-(((__LINE__) << 16) | (-(ret))))
#define ERRCODE(ret)                    ( -((-(ret)) & 0xffff) )
#define CODELINE(ret)                           ( (-(ret))>>16 )
enum{
    Status_Ok           =    0   ,  
    Status_NoSupport    =    -16,
    Status_ParamterErr  =    -17,
    Status_MemAllocErr  =    -30  ,
    Status_GPUError     =    -40  ,
    Status_FileError    =    -50
};


#define Ret_Success             Status_Ok
#define Ret_MemAllocErr         CONVERTCODE(Status_MemAllocErr)
#define Ret_NoSupportErr        CONVERTCODE(Status_NoSupport)
#define Ret_ParamterErr         CONVERTCODE(Status_ParamterErr)
#define Ret_GPUErr              CONVERTCODE(Status_GPUError) 
#define Ret_FileErr             CONVERTCODE(Status_FileError)

#endif