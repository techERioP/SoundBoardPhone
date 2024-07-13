import requests
import os

url = "https://raw.githubusercontent.com/techERioP/SoundBoardPhone/main/serverphoneGUI/build/assets/frame0/button_1.png"
response = requests.get(url)
if response.status_code == 200:
    with open("file.png", "wb") as file:
        if os.path.isfile('file.txt'):
        	print("File already exists.")
        else:
        	file.write(response.content)
        	print("File downloaded successfully!")
else:
    print("Failed to download the file.")