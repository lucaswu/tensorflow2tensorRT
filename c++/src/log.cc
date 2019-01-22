#include "log.h"
#include<memory.h>
#include <stdarg.h>
// void logPrintf(const char *file,const char *func,int line,const char *fmt,...)
// {
// #define BUF_LEN 500
//     char buf[BUF_LEN];
//     va_list args;
//     memset(buf, 0, BUF_LEN);
//     snprintf(buf, BUF_LEN, "[%s:%d]:", file, line, line);
//     va_start(args, fmt);
//     vsnprintf(buf+strlen(buf), BUF_LEN-strlen(buf), fmt, args);
//     va_end(args);
//     printf("%s\n", buf);
// }