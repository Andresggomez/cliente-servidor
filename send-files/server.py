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

    #message = socket.recv_json()
    #message = json.loads(socket.recv())
    # recibir mensaje multipart
    message = socket.recv_multipart()
    print("Received request: %s" % message)

    file_info = message[0]
    file_name = message[1].decode()

    file = open(file_name, 'wb')
    file.write(file_info)

    file.close()

    #  Hacer alguna tarea o proceso
    # time.sleep(1)

    #result = str(task(message))

    #  Enviá respuesta al cliente con el mensaje "World"
    socket.send('completado'.encode())
