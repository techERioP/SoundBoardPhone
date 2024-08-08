import os
import zipfile

with zipfile.ZipFile("buttons_img.zip", 'r', zipfile.ZIP_DEFLATED) as zipf:
    zipf.extractall(path="assets/frame0")