import socket
import os
import pyautogui


# put the phone ip
ipdato = '192.168.1.69'




app_version = 'latest: 3.0'




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connettere():
    try:
        s.connect((str(ipdato), 23081))
    except:
        print("non connesso: sto riprovando")
        connettere()
    else:
        connettere()


try:
    s.connect((str(ipdato), 23081))
except:
    connettere()


full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

    print(full_msg)
    if full_msg == 'button1':
        pyautogui.press('f13')
    elif full_msg == 'button2':
        pyautogui.press('f14')
    elif full_msg == 'button3':
        pyautogui.press('f15')
    elif full_msg == 'button4':
        pyautogui.press('f16')
    elif full_msg == 'button5':
        pyautogui.press('f17')
    elif full_msg == 'button6':
        pyautogui.press('f18')
    elif full_msg == 'button7':
        pyautogui.press('f19')
    elif full_msg == 'button8':
        pyautogui.press('f20')
    elif full_msg == 'button9':
        pyautogui.press('f21')
    elif full_msg == 'button10':
        pyautogui.press('f22')
    elif full_msg == 'button11':
        pyautogui.press('f23')
    elif full_msg == 'button12':
        pyautogui.press('f24')
    elif full_msg == 'button13':
        pyautogui.keyDown('ctrlright')
        pyautogui.press('f20')
        pyautogui.keyUp('ctrlright')
    elif full_msg == 'button14':
        pyautogui.keyDown('ctrlright')
        pyautogui.press('f21')
        pyautogui.keyUp('ctrlright')
    elif full_msg == 'button15':
        pyautogui.keyDown('ctrlright')
        pyautogui.press('f22')
        pyautogui.keyUp('ctrlright')
    elif full_msg == 'button16':
        pyautogui.keyDown('ctrlright')
        pyautogui.press('f23')
        pyautogui.keyUp('ctrlright')
    elif full_msg == 'button18':
        pyautogui.press('volumeup')
    elif full_msg == 'button19':
        pyautogui.press('volumedown')
    else:
        print('prendi una connessione migliore')
