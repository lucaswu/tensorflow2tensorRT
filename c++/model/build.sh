#! /bin/bash
#脚本处理的是把训练的权重、偏置文件以二进制字符串的形式写入到头文件中。对于有子目录的形式，例如A/B,则写入的文件名为A_B
CurrentDir=$PWD
rm -f "$CurrentDir/model.h"

function getdir(){ 
    kernelList=`ls $1`
    for fileName in $kernelList
    do 
       
        dir=$1/$fileName
        if [ -f $dir ];then
            lastfile=${dir#*$PWD/}
            xxd -i $lastfile >> "$CurrentDir/model.h"
            if [ $? -ne 0 ];then
                echo " no $fileName !"
                exit 1
            fi
            
        elif test -d $dir;then
            getdir $dir
        fi
    done

}

echo "#ifndef KSY_MODEL_H_" >> "$CurrentDir/model.h"
echo "#define KSY_MODEL_H_" >> "$CurrentDir/model.h"
getdir $CurrentDir/protobuf

echo "#endif" >> "$CurrentDir/model.h"
