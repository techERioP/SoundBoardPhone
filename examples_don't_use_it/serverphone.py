import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOURCE_PORT, DESTINATION_PORT = 23081, 23081
s.bind(('192.168.1.6', SOURCE_PORT))
s.listen(5)

clientsocket, address = s.accept()
print(f"connection from {address} has been enstablished!")
clientsocket.send(bytes("button10", "utf-8"))
clientsocket.close()