import requests
import pathlib

directory_path = ''
file_name = 'README.md'
url = "https://raw.githubusercontent.com/techERioP/SoundBoardPhone/main/README.md"
response = requests.get(url)

file_path = pathlib.Path(directory_path) / file_name
with open(file_path, 'wb') as file:
    file.write(response.content)
input()