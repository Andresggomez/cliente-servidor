import sys
import zmq

def start_server(server_name):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:5557")

    print("Start Server: %s" % server_name)

    while True:
        message = socket.recv_string()
        print("Receive message = %s" % message)

        reply_message = "Reply %s from %s" % (message, server_name)

        socket.send_string(reply_message)

    socket.close()
    context.destroy()

if __name__ == "__main__":
    start_server(sys.argv[1])
