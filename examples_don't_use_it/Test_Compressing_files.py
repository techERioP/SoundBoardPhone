import os
import zipfile

with zipfile.ZipFile("buttons_img.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
    files = os.listdir("NewButtons")
    for file in files:
        pathfile_italy = str(str("NewButtons/") + str(file))
        with open(pathfile_italy, "rb") as fileboh:
            ciaoo = fileboh.read()
        with open(file, "wb") as fileboh:
            fileboh.write(ciaoo)
        zipf.write(file)
        os.remove(file)