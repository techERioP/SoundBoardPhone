import os
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 23081))
s.listen(5)

clientsocket, address = s.accept()
file_name = clientsocket.recv(1024)
file = open(file_name, "wb")
made_in_ravenna = clientsocket.recv(1)

while made_in_ravenna:
    file.write(made_in_ravenna)
    made_in_ravenna = clientsocket.recv(1)

file.close()
clientsocket.close() 