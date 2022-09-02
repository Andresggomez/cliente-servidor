import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)

#  Conecta al Frontend
#socket.connect("tcp://192.168.2.34:6666)
socket.connect("tcp://*:6666")

while True:
    socket.send("Soy el Cliente1: ".encode('utf-8'))
    message = socket.recv()
    print(message)
    time.sleep(1)
