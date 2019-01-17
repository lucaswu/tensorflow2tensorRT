import tensorrt_pb2

f = open('tensorrt.pb','rb')
net = tensorrt_pb2.NetDef()
net.ParseFromString(f.read())

print("net input:",net.input)
print("net output:",net.output)