import mace_pb2

f = open('tensorrt.pb','rb')
net = mace_pb2.NetDef()
net.ParseFromString(f.read())

print("net input:",net.input)
print("net output:",net.output)