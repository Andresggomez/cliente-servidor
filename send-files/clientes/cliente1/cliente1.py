import zmq
import sys
import time

file_dir = sys.argv[1]  #  Nombre del archivo

context = zmq.Context()

# Cliente hace REQUEST
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")
#  Socket para hablar con el servidor
print("Connecting to File-Server  at port 6666… MAX Size File 10GB")

file_name = input('Nombre de archivo: ')

# Abrimos el archivo de cliente1
fileR = open(file_dir, 'rb')

chunk = 0
byte = fileR.read(1024*1024)  # Tamaño de las partes

while byte:

    fileN = str(file_name) + "chunk" + str(chunk) + ".chk"  # Nombre del archivo archivochunk0.cnk
    fileT = open(fileN, "wb")
    fileT.write(byte)
    fileT.close()

    byte = fileR.read(1024*1024)

    chunk += 1
    #print("creando chunk name : " + fileN)

# Solo para enviar archivos pequeños


time.sleep(3)
count = 0
temp = chunk - 1
while count <= temp:

    fileName = str(file_name) + "chunk" + str(count) + ".chk"
    print(fileName)
    fileTemp = open(fileName, "rb")
    archi_info = fileTemp.read()
    fileTemp.close()

    socket.send_multipart([archi_info, fileName.encode()])

    count +=1

# Respuesta de File-Server
message = socket.recv().decode()
print("File-Server Response [ %s ]: " % message)


