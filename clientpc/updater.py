import socket
import requests
import os
from pathlib import Path


#------------------------------------

#put the clientpc file name with the exestension:
#     |
#     v
ilclient = 'clientpc(2).py'

#------------------------------------



url_latest = 'https://raw.githubusercontent.com/techERioP/SoundBoardPhone/main/clientpc/latest.txt'
response = requests.get(str(url_latest), allow_redirects=False)
with open(str('latest.txt'), "wb") as filetry:
    filetry.write(response.content)


with open('latest.txt', 'r') as file:
    lines = file.read().split('\n')
    version = lines[0]
    files_download = lines[int('1')]
    print('version txt: ' + str(version))


with open(ilclient, 'r') as file:
    lines = file.read().split('\n')
    app_version = lines[11]
    print("app version: " + str(app_version.replace('app_version = ', '')) )


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
        url = "https://raw.githubusercontent.com/techERioP/SoundBoardPhone/main/clientpc/" + str(new_file)
        
        print(url)
        response = requests.get(str(url), allow_redirects=False)
        with open(str(new_file), "wb") as filetry:
            filetry.write(response.content)
    print('---------------------------')
    print('Update done')
    print('Click a key to exit')
    input()
    exit()


def mes_aggiornamento():
    print('------------------------')
    print("Do you want to update to " + version.replace('latest: ', '') + '?')
    print('(type yes or no)')
    risposta = input()
    if risposta == 'yes':
        print('Updating')
        aggiornamento()
    elif risposta == 'no':
        print("click a key to exit")
        input()
        exit()
    else:
        print('risposta invalida')
        mes_aggiornamento()


if version == str(app_version.replace('app_version = ', '')):
    print('------------------------')
    print("version up to date")
    print('Click a key to exit')
    input()
    exit()
elif not version == str(app_version.replace('app_version = ', '')):
    print("version not up to date")
    mes_aggiornamento()
else:
    print("version not up to date")
    mes_aggiornamento()




