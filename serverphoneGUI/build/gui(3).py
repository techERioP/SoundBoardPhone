
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import socket
import requests
import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8''
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

#------------------------------------
# put the phone ip
ipdato = ''
#------------------------------------


linea_numero2 = 1
app_version = 'latest: 3.0'
filename = 'latest.txt'
files_number = '0'
linea_numero = 0
new_file = ''
new_file1 = ''
url = 'https://raw.githubusercontent.com/techERioP/SoundBoardPhone/main/serverphoneGUI/build/latest.txt'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOURCE_PORT, DESTINATION_PORT = 23081, 23081
s.bind((ipdato, SOURCE_PORT))
s.listen(5)


def aggiornamento():
    linea_numero2 = 1
    linea_numero = 0
    while int(linea_numero) < int(files_download):
        with open('latest.txt', 'r') as file:
            lines = file.read().split('\n')
        linea_numero = int(linea_numero) + int(1)
        linea_numero2 = int(linea_numero2) + int(1)
        new_file = lines[linea_numero2]
        print(new_file)
        url = "https://raw.githubusercontent.com/techERioP/SoundBoardPhone/main/serverphoneGUI/build/" + \
            str(new_file)
        print(url)
        response = requests.get(str(url), allow_redirects=False)
        with open(str(new_file), "wb") as filetry:
            filetry.write(response.content)

    print("update done")
    messagebox.showinfo("Update done", "Update " + version.replace('latest: ', '') + " done")


def mes_aggiornamento():
    if messagebox.askyesno("Update found", "Do you want to update to " + version.replace("latest: ", "") + "?"):
        print("user choose yes")
        aggiornamento()
    else:
        print("user choose no")


def mes_delversion():
    if messagebox.askyesno("Old version found", "Do you want remove 2.0 version?"):
        os.remove('gui(2).py')
        exit()

    else:
        print("")


response = requests.get(url)
if response.status_code == 200:
    with open("latest.txt", "wb") as file:
        file.write(response.content)


with open('latest.txt', 'r') as file:
    lines = file.read().split('\n')
    version = lines[0]
    files_download = lines[int('1')]
    print(version)
if version == app_version:
    print("version up to date")
else:
    print("version not up to date")
    mes_aggiornamento()

if os.path.exists('gui(2).py'):
    mes_delversion()
else:
    print("")


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def button1():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button1", "utf-8"))
    clientsocket.close()


def button2():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button2", "utf-8"))
    clientsocket.close()


def button3():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button3", "utf-8"))
    clientsocket.close()


def button4():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button4", "utf-8"))
    clientsocket.close()


def button5():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button5", "utf-8"))
    clientsocket.close()


def button6():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button6", "utf-8"))
    clientsocket.close()


def button7():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button7", "utf-8"))
    clientsocket.close()


def button8():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button8", "utf-8"))
    clientsocket.close()


def button9():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button9", "utf-8"))
    clientsocket.close()


def button10():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button10", "utf-8"))
    clientsocket.close()


def button11():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button11", "utf-8"))
    clientsocket.close()


def button12():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button12", "utf-8"))
    clientsocket.close()


def button13():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button13", "utf-8"))
    clientsocket.close()


def button14():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button14", "utf-8"))
    clientsocket.close()


def button15():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button15", "utf-8"))
    clientsocket.close()


def button16():

    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button16", "utf-8"))
    clientsocket.close()


def button17():
    exit()


def button18():
    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button18", "utf-8"))
    clientsocket.close()


def button19():
    clientsocket, address = s.accept()
    print(f"connection from {address} has been enstablished!")
    clientsocket.send(bytes("button19", "utf-8"))
    clientsocket.close()


window = Tk()

window.geometry("1080x1920")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1920,
    width=1080,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button11,
    relief="flat"
)
button_1.place(
    x=30.0,
    y=56.0,
    width=272.0,
    height=256.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button6,
    relief="flat"
)
button_2.place(
    x=397.0,
    y=56.0,
    width=272.0,
    height=256.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button1,
    relief="flat"
)
button_3.place(
    x=780.0,
    y=56.0,
    width=272.0,
    height=256.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=button12,
    relief="flat"
)
button_4.place(
    x=29.0,
    y=402.0,
    width=272.0,
    height=256.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=button15,
    relief="flat"
)
button_5.place(
    x=30.0,
    y=1384.0,
    width=272.0,
    height=256.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=button10,
    relief="flat"
)
button_6.place(
    x=397.0,
    y=1384.0,
    width=272.0,
    height=256.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=button5,
    relief="flat"
)
button_7.place(
    x=780.0,
    y=1384.0,
    width=272.0,
    height=256.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=button13,
    relief="flat"
)
button_8.place(
    x=29.0,
    y=727.0,
    width=272.0,
    height=256.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=button8,
    relief="flat"
)
button_9.place(
    x=397.0,
    y=727.0,
    width=272.0,
    height=256.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=button7,
    relief="flat"
)
button_10.place(
    x=397.0,
    y=392.0,
    width=272.0,
    height=256.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=button3,
    relief="flat"
)
button_11.place(
    x=780.0,
    y=727.0,
    width=272.0,
    height=256.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=button2,
    relief="flat"
)
button_12.place(
    x=780.0,
    y=392.0,
    width=272.0,
    height=256.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=button4,
    relief="flat"
)
button_13.place(
    x=780.0,
    y=1059.0,
    width=272.0,
    height=256.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=button14,
    relief="flat"
)
button_14.place(
    x=30.0,
    y=1048.0,
    width=272.0,
    height=256.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=button9,
    relief="flat"
)
button_15.place(
    x=397.0,
    y=1056.0,
    width=272.0,
    height=256.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=button16,
    relief="flat"
)
button_16.place(
    x=77.0,
    y=1704.0,
    width=176.0,
    height=176.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=button17,
    relief="flat"
)
button_17.place(
    x=921.0,
    y=1724.0,
    width=135.0,
    height=135.0
)


button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=button18,
    relief="flat"
)
button_18.place(
    x=615.0,
    y=1655.0,
    width=218.0,
    height=265.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=button19,
    relief="flat"
)
button_19.place(
    x=340.0,
    y=1655.0,
    width=218.0,
    height=265.0
)

os.remove("latest.txt")

window.resizable(False, False)
window.mainloop()
