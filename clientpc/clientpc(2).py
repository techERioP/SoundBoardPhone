import socket
import pyautogui


#put the phone ip
ipdato = '192.168.1.4'




#version of the app
app_version = 'latest: 2.0'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connettere():
    try:
        s.connect((ipdato, 23081))
    except:
        print("non connesso: sto riprovando")
        connettere()
    else:
        connettere()

try:
    s.connect((ipdato, 23081))
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
		pyautogui.press('num1')
	elif full_msg == 'button2':
		pyautogui.press('num2')
	elif full_msg == 'button3':
		pyautogui.press('num3')
	elif full_msg == 'button4':
		pyautogui.press('num4')
	elif full_msg == 'button5':
		pyautogui.press('num5')
	elif full_msg == 'button6':
		pyautogui.press('num6')
	elif full_msg == 'button7':
		pyautogui.press('num7')
	elif full_msg == 'button8':
		pyautogui.press('num8')
	elif full_msg == 'button9':
		pyautogui.press('num9')
	elif full_msg == 'button10':
		pyautogui.press('.')
	elif full_msg == 'button11':
		pyautogui.press('+')
	elif full_msg == 'button12':
		pyautogui.press('left')
	elif full_msg == 'button13':
		pyautogui.press('right')
	elif full_msg == 'button14':
		pyautogui.press(',')
	elif full_msg == 'button15':
		pyautogui.press('-')
	elif full_msg == 'button16':
		pyautogui.press('num0')
	elif full_msg == 'button18':
		pyautogui.press('volumeup')
	elif full_msg == 'button19':
		pyautogui.press('volumedown')
	else:
		print('prendi una connessione migliore')