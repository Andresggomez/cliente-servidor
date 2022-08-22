import zmq
import json
import sys

file_dir = sys.argv[1]

context = zmq.Context()

#  Socket para hablar con el servidor
print("Connecting to Server 1 at port 6666…")


# Cliente hace REQUEST
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")

file_name = input('Nombre de archivo: ')

# Solo para enviar archivos pequeños
file = open(file_dir, 'rb')
archi_info = file.read()  #leer el archivo en memoria

print("Enviando Archivo...")
#socket.send_string(json.dumps(lista))
socket.send_multipart([archi_info, file_name.encode()])
file.close()

#  Get the reply.
message = socket.recv().decode()
print("Received reply [ %s ]" % message)


