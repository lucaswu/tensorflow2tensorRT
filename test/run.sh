#! /bin/sh

CurrentDir=$PWD

protoc --python_out=${CurrentDir}/../python/tools  --proto_path=${CurrentDir}/../proto/ ${CurrentDir}/../proto/mace.proto
echo "protoc success"
python3 ${CurrentDir}/../python/tools/converter.py --model_file=$CurrentDir/../test/32bit_1080p_yuv.pb --input_node=src_input_1,src_input_2,src_input_3 --input_shape=1,1920,1080,1:1,960,540,1:1,960,540,1 --input_shape_base=1,1920,1080,1 --output_node=SR_TV/imgout_1,SR_TV/imgout_2,SR_TV/imgout_3 --output_shape=1,1920,1080,1:1,960,540,1:1,960,540,1 

# mv tensorrt.*  ${CurrentDir}/../../sr_server_sdk/model/protobuf
# cp ${CurrentDir}/../proto/mace.proto ${CurrentDir}/../../sr_server_sdk/proto