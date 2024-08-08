import os
import socket
import zipfile

print("Put the phone IP and then open the ChangeButtonsImgPC.py on Computer")
ipdato = input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipdato, 23081))
s.listen(5)

clientsocket, address = s.accept()
file = open("buttons_img.zip", "wb")
made_in_ravenna = clientsocket.recv(2048)

while made_in_ravenna:
    file.write(made_in_ravenna)
    made_in_ravenna = clientsocket.recv(2048)

print(os.system("unzip -o buttons_img.zip"))
print("\n------------------------\nChanging images done\n------------------------")

file.close()
clientsocket.close() 