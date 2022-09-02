#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back

import zmq
import json

context = zmq.Context()

#  Socket para hablar con el servidor
print("Connecting to Server 1 at port 5555…")

# Cliente hace REQUEST
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
list = ['+', 4, 7]

print("Sending request")
#socket.send_string(json.dumps(lista))
socket.send_json(list)
#  Get the reply.
message = socket.recv()
print("Received reply [ %s ]" % message)
