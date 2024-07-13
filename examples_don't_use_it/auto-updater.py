import os

file_path = 'reading_and_del_txt_file.py'
version = 'latest: 1.0'
with open('prova.txt', 'r') as f:
    content = f.read()
print(content)
if content == version:
     print("version up-to-date")
     input()
else:
     os.remove(file_path)
     print("File has been deleted")
     input()




