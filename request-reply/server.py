#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello clienteN" from client, replies with b"World"

import time
import zmq
import json

context = zmq.Context()
# Servidor hace REPLY
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Servidor Online... Port 5555")

#  Espera por el siguiente mensaje de algún cliente

while True:

    # Trae el mensaje desde el cliente que se conecta al puerto
    message = socket.recv_json()
    #message = json.loads(socket.recv())
    print("Received request: %s" % message)

    #  Hacer alguna tarea o proceso
    # time.sleep(1)

    def multi(info):
        ope = info[0]
        if ope == '+':
            resp = info[1] + info[2]
            return resp

        elif ope == '*':
            resp = info[1] * info[2]
            return resp

        elif ope == '/':
            resp = info[1] / info[2]
            return resp

        elif ope == '-':
            resp = info[1] - info[2]
            return resp

        elif ope != -1:
            resp = 'Error de operacion'
            return resp

    result = str(multi(message))

    #  Enviá respuesta al cliente con el mensaje "World"
    socket.send_string(result)

print("Servidor Online... Port 5555")
