import time
import zmq
import json

context = zmq.Context()
# Servidor hace REPLY
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

print("Servidor Online... Port 6666")

#  Espera por el siguiente mensaje de algún cliente

while True:

    # Trae el mensaje desde el cliente que se conecta al puerto

    message = socket.recv_multipart()
    print("Received request:")

    file_info = message[0]
    file_name = message[1].decode()

    file = open(file_name, 'wb')

    file.write(file_info)
    file.close()

socket.send('Se recivio el archivo corectamente'.encode())
print("Request completd")
