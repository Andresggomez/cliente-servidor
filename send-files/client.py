import zmq
import json

context = zmq.Context()

#  Socket para hablar con el servidor
print("Connecting to Server 1 at port 6666…")

# Cliente hace REQUEST
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")

file_name = input('Nombre de archivo: ')
file = open('Archivo1.txt', 'rb')
archi_info = file.read()

print("Sending request")
#socket.send_string(json.dumps(lista))
socket.send_multipart([archi_info, file_name.encode()])
file.close()

#  Get the reply.
message = socket.recv().decode()
print("Received reply [ %s ]" % message)


