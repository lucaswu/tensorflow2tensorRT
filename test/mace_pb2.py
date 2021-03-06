# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mace.proto',
  package='mace',
  syntax='proto2',
  serialized_pb=_b('\n\nmace.proto\x12\x04mace\"\xf9\x01\n\x0b\x43onstTensor\x12\x0c\n\x04\x64ims\x18\x01 \x03(\x03\x12-\n\tdata_type\x18\x02 \x01(\x0e\x32\x10.mace.TensorType:\x08\x44T_FLOAT\x12\x16\n\nfloat_data\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x16\n\nint32_data\x18\x04 \x03(\x05\x42\x02\x10\x01\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0e\n\x06offset\x18\x06 \x01(\x03\x12\x11\n\tdata_size\x18\x07 \x01(\x03\x12\r\n\x05scale\x18\x08 \x01(\x02\x12\x12\n\nzero_point\x18\t \x01(\x05\x12\x18\n\tquantized\x18\n \x01(\x08:\x05\x66\x61lse\x12\x0f\n\x07node_id\x18\x64 \x01(\r\"W\n\x08\x41rgument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\t\n\x01\x66\x18\x02 \x01(\x02\x12\t\n\x01i\x18\x03 \x01(\x03\x12\t\n\x01s\x18\x04 \x01(\x0c\x12\x0e\n\x06\x66loats\x18\x05 \x03(\x02\x12\x0c\n\x04ints\x18\x06 \x03(\x03\"1\n\tNodeInput\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x13\n\x0boutput_port\x18\x02 \x01(\x05\"\x1b\n\x0bOutputShape\x12\x0c\n\x04\x64ims\x18\x01 \x03(\x03\"[\n\x16QuantizeActivationInfo\x12\r\n\x05scale\x18\x01 \x01(\x02\x12\x12\n\nzero_point\x18\x02 \x01(\x05\x12\x0e\n\x06minval\x18\x03 \x01(\x02\x12\x0e\n\x06maxval\x18\x04 \x01(\x02\"\xeb\x02\n\x0bOperatorDef\x12\r\n\x05input\x18\x01 \x03(\t\x12\x0e\n\x06output\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x1b\n\x03\x61rg\x18\x05 \x03(\x0b\x32\x0e.mace.Argument\x12\'\n\x0coutput_shape\x18\x06 \x03(\x0b\x32\x11.mace.OutputShape\x12%\n\x0boutput_type\x18\x07 \x03(\x0e\x32\x10.mace.TensorType\x12\x33\n\rquantize_info\x18\x08 \x03(\x0b\x32\x1c.mace.QuantizeActivationInfo\x12\x0e\n\x06mem_id\x18\n \x03(\x05\x12\x0f\n\x07node_id\x18\x64 \x01(\r\x12\r\n\x05op_id\x18\x65 \x01(\r\x12\x0f\n\x07padding\x18\x66 \x01(\r\x12#\n\nnode_input\x18g \x03(\x0b\x32\x0f.mace.NodeInput\x12\x19\n\x11out_max_byte_size\x18h \x03(\x05\"l\n\x0bMemoryBlock\x12\x0e\n\x06mem_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65vice_type\x18\x02 \x01(\x05\x12\"\n\x08mem_type\x18\x03 \x01(\x0e\x32\x10.mace.MemoryType\x12\t\n\x01x\x18\x04 \x01(\r\x12\t\n\x01y\x18\x05 \x01(\r\"3\n\x0bMemoryArena\x12$\n\tmem_block\x18\x01 \x03(\x0b\x32\x11.mace.MemoryBlock\"~\n\tInputInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\x12\x0c\n\x04\x64ims\x18\x03 \x03(\x05\x12\x15\n\rmax_byte_size\x18\x04 \x01(\x05\x12-\n\tdata_type\x18\x05 \x01(\x0e\x32\x10.mace.TensorType:\x08\x44T_FLOAT\"\x7f\n\nOutputInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\x12\x0c\n\x04\x64ims\x18\x03 \x03(\x05\x12\x15\n\rmax_byte_size\x18\x04 \x01(\x05\x12-\n\tdata_type\x18\x05 \x01(\x0e\x32\x10.mace.TensorType:\x08\x44T_FLOAT\"\x98\x02\n\x06NetDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x02op\x18\x02 \x03(\x0b\x32\x11.mace.OperatorDef\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x1b\n\x03\x61rg\x18\x04 \x03(\x0b\x32\x0e.mace.Argument\x12\"\n\x07tensors\x18\x05 \x03(\x0b\x32\x11.mace.ConstTensor\x12\r\n\x05input\x18\x06 \x03(\t\x12\x0e\n\x06output\x18\x07 \x03(\t\x12$\n\tmem_arena\x18\n \x01(\x0b\x32\x11.mace.MemoryArena\x12#\n\ninput_info\x18\x64 \x03(\x0b\x32\x0f.mace.InputInfo\x12%\n\x0boutput_info\x18\x65 \x03(\x0b\x32\x10.mace.OutputInfo*\x1f\n\x07NetMode\x12\x08\n\x04INIT\x10\x00\x12\n\n\x06NORMAL\x10\x01*S\n\nTensorType\x12\x0e\n\nDT_INVALID\x10\x00\x12\x0c\n\x08\x44T_FLOAT\x10\x01\x12\x0c\n\x08\x44T_UINT8\x10\x02\x12\x0b\n\x07\x44T_HALF\x10\x03\x12\x0c\n\x08\x44T_INT32\x10\x04*;\n\nMemoryType\x12\x0e\n\nCPU_BUFFER\x10\x00\x12\x0e\n\nGPU_BUFFER\x10\x01\x12\r\n\tGPU_IMAGE\x10\x02\x42\x02H\x03')
)

_NETMODE = _descriptor.EnumDescriptor(
  name='NetMode',
  full_name='mace.NetMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1603,
  serialized_end=1634,
)
_sym_db.RegisterEnumDescriptor(_NETMODE)

NetMode = enum_type_wrapper.EnumTypeWrapper(_NETMODE)
_TENSORTYPE = _descriptor.EnumDescriptor(
  name='TensorType',
  full_name='mace.TensorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DT_INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_FLOAT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT8', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_HALF', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT32', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1636,
  serialized_end=1719,
)
_sym_db.RegisterEnumDescriptor(_TENSORTYPE)

TensorType = enum_type_wrapper.EnumTypeWrapper(_TENSORTYPE)
_MEMORYTYPE = _descriptor.EnumDescriptor(
  name='MemoryType',
  full_name='mace.MemoryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CPU_BUFFER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPU_BUFFER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPU_IMAGE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1721,
  serialized_end=1780,
)
_sym_db.RegisterEnumDescriptor(_MEMORYTYPE)

MemoryType = enum_type_wrapper.EnumTypeWrapper(_MEMORYTYPE)
INIT = 0
NORMAL = 1
DT_INVALID = 0
DT_FLOAT = 1
DT_UINT8 = 2
DT_HALF = 3
DT_INT32 = 4
CPU_BUFFER = 0
GPU_BUFFER = 1
GPU_IMAGE = 2



_CONSTTENSOR = _descriptor.Descriptor(
  name='ConstTensor',
  full_name='mace.ConstTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='mace.ConstTensor.dims', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='mace.ConstTensor.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_data', full_name='mace.ConstTensor.float_data', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32_data', full_name='mace.ConstTensor.int32_data', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mace.ConstTensor.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='mace.ConstTensor.offset', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_size', full_name='mace.ConstTensor.data_size', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='mace.ConstTensor.scale', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zero_point', full_name='mace.ConstTensor.zero_point', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantized', full_name='mace.ConstTensor.quantized', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='mace.ConstTensor.node_id', index=10,
      number=100, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=270,
)


_ARGUMENT = _descriptor.Descriptor(
  name='Argument',
  full_name='mace.Argument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mace.Argument.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f', full_name='mace.Argument.f', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i', full_name='mace.Argument.i', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s', full_name='mace.Argument.s', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floats', full_name='mace.Argument.floats', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ints', full_name='mace.Argument.ints', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=359,
)


_NODEINPUT = _descriptor.Descriptor(
  name='NodeInput',
  full_name='mace.NodeInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='mace.NodeInput.node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_port', full_name='mace.NodeInput.output_port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=410,
)


_OUTPUTSHAPE = _descriptor.Descriptor(
  name='OutputShape',
  full_name='mace.OutputShape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='mace.OutputShape.dims', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=439,
)


_QUANTIZEACTIVATIONINFO = _descriptor.Descriptor(
  name='QuantizeActivationInfo',
  full_name='mace.QuantizeActivationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scale', full_name='mace.QuantizeActivationInfo.scale', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zero_point', full_name='mace.QuantizeActivationInfo.zero_point', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minval', full_name='mace.QuantizeActivationInfo.minval', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxval', full_name='mace.QuantizeActivationInfo.maxval', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=532,
)


_OPERATORDEF = _descriptor.Descriptor(
  name='OperatorDef',
  full_name='mace.OperatorDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='mace.OperatorDef.input', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='mace.OperatorDef.output', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mace.OperatorDef.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='mace.OperatorDef.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg', full_name='mace.OperatorDef.arg', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_shape', full_name='mace.OperatorDef.output_shape', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_type', full_name='mace.OperatorDef.output_type', index=6,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantize_info', full_name='mace.OperatorDef.quantize_info', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mem_id', full_name='mace.OperatorDef.mem_id', index=8,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='mace.OperatorDef.node_id', index=9,
      number=100, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_id', full_name='mace.OperatorDef.op_id', index=10,
      number=101, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='padding', full_name='mace.OperatorDef.padding', index=11,
      number=102, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_input', full_name='mace.OperatorDef.node_input', index=12,
      number=103, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_max_byte_size', full_name='mace.OperatorDef.out_max_byte_size', index=13,
      number=104, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=898,
)


_MEMORYBLOCK = _descriptor.Descriptor(
  name='MemoryBlock',
  full_name='mace.MemoryBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mem_id', full_name='mace.MemoryBlock.mem_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='mace.MemoryBlock.device_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mem_type', full_name='mace.MemoryBlock.mem_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='mace.MemoryBlock.x', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mace.MemoryBlock.y', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=900,
  serialized_end=1008,
)


_MEMORYARENA = _descriptor.Descriptor(
  name='MemoryArena',
  full_name='mace.MemoryArena',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mem_block', full_name='mace.MemoryArena.mem_block', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1010,
  serialized_end=1061,
)


_INPUTINFO = _descriptor.Descriptor(
  name='InputInfo',
  full_name='mace.InputInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mace.InputInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='mace.InputInfo.node_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dims', full_name='mace.InputInfo.dims', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_byte_size', full_name='mace.InputInfo.max_byte_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='mace.InputInfo.data_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1063,
  serialized_end=1189,
)


_OUTPUTINFO = _descriptor.Descriptor(
  name='OutputInfo',
  full_name='mace.OutputInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mace.OutputInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='mace.OutputInfo.node_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dims', full_name='mace.OutputInfo.dims', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_byte_size', full_name='mace.OutputInfo.max_byte_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='mace.OutputInfo.data_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1191,
  serialized_end=1318,
)


_NETDEF = _descriptor.Descriptor(
  name='NetDef',
  full_name='mace.NetDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mace.NetDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='mace.NetDef.op', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='mace.NetDef.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg', full_name='mace.NetDef.arg', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensors', full_name='mace.NetDef.tensors', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='mace.NetDef.input', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='mace.NetDef.output', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mem_arena', full_name='mace.NetDef.mem_arena', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_info', full_name='mace.NetDef.input_info', index=8,
      number=100, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_info', full_name='mace.NetDef.output_info', index=9,
      number=101, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1321,
  serialized_end=1601,
)

_CONSTTENSOR.fields_by_name['data_type'].enum_type = _TENSORTYPE
_OPERATORDEF.fields_by_name['arg'].message_type = _ARGUMENT
_OPERATORDEF.fields_by_name['output_shape'].message_type = _OUTPUTSHAPE
_OPERATORDEF.fields_by_name['output_type'].enum_type = _TENSORTYPE
_OPERATORDEF.fields_by_name['quantize_info'].message_type = _QUANTIZEACTIVATIONINFO
_OPERATORDEF.fields_by_name['node_input'].message_type = _NODEINPUT
_MEMORYBLOCK.fields_by_name['mem_type'].enum_type = _MEMORYTYPE
_MEMORYARENA.fields_by_name['mem_block'].message_type = _MEMORYBLOCK
_INPUTINFO.fields_by_name['data_type'].enum_type = _TENSORTYPE
_OUTPUTINFO.fields_by_name['data_type'].enum_type = _TENSORTYPE
_NETDEF.fields_by_name['op'].message_type = _OPERATORDEF
_NETDEF.fields_by_name['arg'].message_type = _ARGUMENT
_NETDEF.fields_by_name['tensors'].message_type = _CONSTTENSOR
_NETDEF.fields_by_name['mem_arena'].message_type = _MEMORYARENA
_NETDEF.fields_by_name['input_info'].message_type = _INPUTINFO
_NETDEF.fields_by_name['output_info'].message_type = _OUTPUTINFO
DESCRIPTOR.message_types_by_name['ConstTensor'] = _CONSTTENSOR
DESCRIPTOR.message_types_by_name['Argument'] = _ARGUMENT
DESCRIPTOR.message_types_by_name['NodeInput'] = _NODEINPUT
DESCRIPTOR.message_types_by_name['OutputShape'] = _OUTPUTSHAPE
DESCRIPTOR.message_types_by_name['QuantizeActivationInfo'] = _QUANTIZEACTIVATIONINFO
DESCRIPTOR.message_types_by_name['OperatorDef'] = _OPERATORDEF
DESCRIPTOR.message_types_by_name['MemoryBlock'] = _MEMORYBLOCK
DESCRIPTOR.message_types_by_name['MemoryArena'] = _MEMORYARENA
DESCRIPTOR.message_types_by_name['InputInfo'] = _INPUTINFO
DESCRIPTOR.message_types_by_name['OutputInfo'] = _OUTPUTINFO
DESCRIPTOR.message_types_by_name['NetDef'] = _NETDEF
DESCRIPTOR.enum_types_by_name['NetMode'] = _NETMODE
DESCRIPTOR.enum_types_by_name['TensorType'] = _TENSORTYPE
DESCRIPTOR.enum_types_by_name['MemoryType'] = _MEMORYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConstTensor = _reflection.GeneratedProtocolMessageType('ConstTensor', (_message.Message,), dict(
  DESCRIPTOR = _CONSTTENSOR,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.ConstTensor)
  ))
_sym_db.RegisterMessage(ConstTensor)

Argument = _reflection.GeneratedProtocolMessageType('Argument', (_message.Message,), dict(
  DESCRIPTOR = _ARGUMENT,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.Argument)
  ))
_sym_db.RegisterMessage(Argument)

NodeInput = _reflection.GeneratedProtocolMessageType('NodeInput', (_message.Message,), dict(
  DESCRIPTOR = _NODEINPUT,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.NodeInput)
  ))
_sym_db.RegisterMessage(NodeInput)

OutputShape = _reflection.GeneratedProtocolMessageType('OutputShape', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTSHAPE,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.OutputShape)
  ))
_sym_db.RegisterMessage(OutputShape)

QuantizeActivationInfo = _reflection.GeneratedProtocolMessageType('QuantizeActivationInfo', (_message.Message,), dict(
  DESCRIPTOR = _QUANTIZEACTIVATIONINFO,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.QuantizeActivationInfo)
  ))
_sym_db.RegisterMessage(QuantizeActivationInfo)

OperatorDef = _reflection.GeneratedProtocolMessageType('OperatorDef', (_message.Message,), dict(
  DESCRIPTOR = _OPERATORDEF,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.OperatorDef)
  ))
_sym_db.RegisterMessage(OperatorDef)

MemoryBlock = _reflection.GeneratedProtocolMessageType('MemoryBlock', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYBLOCK,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.MemoryBlock)
  ))
_sym_db.RegisterMessage(MemoryBlock)

MemoryArena = _reflection.GeneratedProtocolMessageType('MemoryArena', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYARENA,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.MemoryArena)
  ))
_sym_db.RegisterMessage(MemoryArena)

InputInfo = _reflection.GeneratedProtocolMessageType('InputInfo', (_message.Message,), dict(
  DESCRIPTOR = _INPUTINFO,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.InputInfo)
  ))
_sym_db.RegisterMessage(InputInfo)

OutputInfo = _reflection.GeneratedProtocolMessageType('OutputInfo', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTINFO,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.OutputInfo)
  ))
_sym_db.RegisterMessage(OutputInfo)

NetDef = _reflection.GeneratedProtocolMessageType('NetDef', (_message.Message,), dict(
  DESCRIPTOR = _NETDEF,
  __module__ = 'tensorrt_pb2'
  # @@protoc_insertion_point(class_scope:mace.NetDef)
  ))
_sym_db.RegisterMessage(NetDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
_CONSTTENSOR.fields_by_name['float_data'].has_options = True
_CONSTTENSOR.fields_by_name['float_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_CONSTTENSOR.fields_by_name['int32_data'].has_options = True
_CONSTTENSOR.fields_by_name['int32_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
