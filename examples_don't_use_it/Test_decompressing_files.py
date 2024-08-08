import os
import zipfile

with zipfile.ZipFile("buttons_img.zip", 'r', zipfile.ZIP_DEFLATED) as zipf:
    zipf.extractall(path="assets/frame0")

#only works on pc, on pydroid or linux use (runs a command on terminal) os.system(unzip ciaoo.zip -o)