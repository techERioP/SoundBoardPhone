import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 23081))

file_name = '2.png'
client.send(bytes(file_name, "utf-8"))
file = open("1.png", "rb")
image_italy = file.read(2048)

while image_italy:
    client.send(image_italy)
    image_italy = file.read(2048)
    

file.close()
client.close() 