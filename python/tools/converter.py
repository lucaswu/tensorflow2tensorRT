# Copyright 2018 Xiaomi, Inc.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys
import hashlib
import os.path
import copy

import mace_pb2
import model_saver
from converter_tool import base_converter as cvt
from converter_tool import transformer
from convert_util import mace_check


# ./bazel-bin/mace/python/tools/tf_converter --model_file quantized_test.pb \
#                                            --output quantized_test_dsp.pb \
#                                            --runtime dsp \
#                                            --input_dim input_node,1,28,28,3

FLAGS = None

def parse_data_type(data_type):
    if data_type == 'fp32_fp32':
        return mace_pb2.DT_FLOAT
    else:
        return mace_pb2.DT_HALF
    

def file_checksum(fname):
    hash_func = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def parse_int_array_from_str(ints_str):
    return [int(int_str) for int_str in ints_str.split(',')]


def parse_float_array_from_str(ints_str):
    return [float(int_str) for int_str in ints_str.split(',')]


def main(unused_args):
    if not os.path.isfile(FLAGS.model_file):
        print("Input graph file '" + FLAGS.model_file + "' does not exist!")
        sys.exit(-1)

   
    if FLAGS.platform not in ['tensorflow', 'caffe']:
        print ("platform %s is not supported." % FLAGS.platform)
        sys.exit(-1)
    if FLAGS.runtime not in ['cpu', 'gpu', 'dsp', 'cpu+gpu']:
        print ("runtime %s is not supported." % FLAGS.runtime)
        sys.exit(-1)

    option = cvt.ConverterOption()
    if FLAGS.graph_optimize_options:
        option.transformer_option = FLAGS.graph_optimize_options.split(',')
    # option.winograd = FLAGS.winograd
    # option.quantize = FLAGS.quantize
    # option.quantize_range_file = FLAGS.quantize_range_file
    # option.cl_mem_type = FLAGS.cl_mem_type

    input_node_names = FLAGS.input_node.split(',')
    input_node_shapes = FLAGS.input_shape.split(':')
    if FLAGS.input_range:
        input_node_ranges = FLAGS.input_range.split(':')
    else:
        input_node_ranges = []
    if len(input_node_names) != len(input_node_shapes):
        raise Exception('input node count and shape count do not match.')
    for i in range(len(input_node_names)):
        input_node = cvt.NodeInfo()
        input_node.name = input_node_names[i]
        input_node.shape = parse_int_array_from_str(input_node_shapes[i])
        if len(input_node_ranges) > i:
            input_node.range = parse_float_array_from_str(input_node_ranges[i])
        option.add_input_node(input_node)

    output_node_names = FLAGS.output_node.split(',')
    for i in range(len(output_node_names)):
        output_node = cvt.NodeInfo()
        output_node.name = output_node_names[i]
        option.add_output_node(output_node)

    option.base_shape = parse_int_array_from_str(FLAGS.input_shape_base)
    option.build()

    print("Transform model to one that can better run on device")
    if FLAGS.platform == 'tensorflow':
        from converter_tool import tensorflow_converter
        converter = tensorflow_converter.TensorflowConverter(
            option, FLAGS.model_file)
    else:
        print("Mace do not support platorm %s yet." & FLAGS.platform)
        exit(1)

    output_graph_def = converter.run()

    option.device = cvt.DeviceType.GPU.value
    option.data_type = parse_data_type(FLAGS.data_type)
    mace_transformer = transformer.Transformer(option, output_graph_def)
    output_graph_def = mace_transformer.run()

    model_saver.save_model(
        output_graph_def, '', '',
        FLAGS.template_dir, FLAGS.obfuscate, FLAGS.model_tag,
        FLAGS.output_dir, FLAGS.runtime,
        FLAGS.embed_model_data,
        FLAGS.winograd, FLAGS.data_type,
        FLAGS.model_graph_format)

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parse_args():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument(
        "--model_file",
        type=str,
        default="",
        help="TensorFlow \'GraphDef\' file to load, "
        "Caffe prototxt file to load.")
    # parser.add_argument(
    #     "--weight_file", type=str, default="", help="Caffe data file to load.")
    # parser.add_argument(
    #     "--model_checksum",
    #     type=str,
    #     default="",
    #     help="Model file sha256 checksum")
    # parser.add_argument(
    #     "--weight_checksum",
    #     type=str,
    #     default="",
    #     help="Weight file sha256 checksum")
    parser.add_argument(
        "--output_dir",
        type=str,
        default="",
        help="File to save the output graph to.")
    parser.add_argument(
        "--runtime", type=str, default="gpu", help="Runtime: cpu/gpu/dsp")
    parser.add_argument(
        "--input_node",
        type=str,
        default="input_node",
        help="e.g., input_node")
    parser.add_argument(
        "--output_node", type=str, default="softmax", help="e.g., softmax")
    parser.add_argument(
        "--template_dir", type=str, default="", help="template path")
    parser.add_argument(
        "--obfuscate",
        type=str2bool,
        nargs='?',
        const=False,
        default=False,
        help="obfuscate model names")
    parser.add_argument(
        "--model_tag",
        type=str,
        default="tensorrt",
        help="model tag for generated function and namespace")
    parser.add_argument(
        "--winograd",
        type=int,
        default=0,
        help="Which version of winograd convolution to use. [2 | 4]")
    # parser.add_argument(
    #     "--dsp_mode", type=int, default=0, help="dsp run mode, defalut=0")
    parser.add_argument(
        "--input_shape", type=str, default="", help="input shape.")
    parser.add_argument("--input_shape_base", type=str, default="", help="input shape base")
    parser.add_argument(
        "--input_range", type=str, default="", help="input range.")
    parser.add_argument(
        "--platform", type=str, default="tensorflow", help="tensorflow/caffe")
    parser.add_argument(
        "--embed_model_data",
        type=str2bool,
        default=True,
        help="embed model data.")
    parser.add_argument(
        "--model_graph_format",
        type=str,
        default="file",
        help="[file|code] build models to code" +
                "or `Protobuf` file.")
    parser.add_argument(
        "--data_type",
        type=str,
        default="fp32_fp32",
        help="fp16_fp32/fp32_fp32")
    parser.add_argument(
        "--graph_optimize_options",
        type=str,
        default="",
        help="graph optimize options")
    # parser.add_argument(
    #     "--quantize",
    #     type=str2bool,
    #     nargs='?',
    #     const=False,
    #     default=False,
    #     help="quantize model")
    # parser.add_argument(
    #     "--quantize_range_file",
    #     type=str,
    #     default="",
    #     help="file path of quantize range for each tensor")
    # parser.add_argument(
    #     "--cl_mem_type",
    #     type=str,
    #     default="image",
    #     help="which memory type to use.[image|buffer]")
    return parser.parse_known_args()


if __name__ == '__main__':
    FLAGS, unparsed = parse_args()
    main(unused_args=[sys.argv[0]] + unparsed)
