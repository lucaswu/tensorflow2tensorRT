#! /bin/sh
CurrentDir=$PWD

cd ../build
make clean

make 
if [ $? -ne 0 ];then
  echo "build  error !"
  exit 1
fi

./test