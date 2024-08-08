import os
import socket
from PIL import Image
import zipfile
import tkinter


#put the phone ip
print("Open ChangeButtonImgPhone.py on pydroid and then type phone IP")
ipdato = input()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipdato, 23081))

if not os.path.exists("assets/frame0"):
    os.makedirs("assets/frame0")
    print("directory maked")

while True:
    if os.path.exists("NewButtons/1.png"):
        print("1.png exists")
        image_ita = "NewButtons/1.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_3.png")
        os.remove("NewButtons/1.png")
    elif os.path.exists("NewButtons/2.png"):
        print("2.png exists")
        image_ita = "NewButtons/2.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_12.png")
        os.remove("NewButtons/2.png")
    elif os.path.exists("NewButtons/3.png"):
        print("3.png exists")
        image_ita = "NewButtons/3.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_11.png")
        os.remove("NewButtons/3.png")
    elif os.path.exists("NewButtons/4.png"):
        print("4.png exists")
        image_ita = "NewButtons/4.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_13.png")
        os.remove("NewButtons/4.png")
    elif os.path.exists("NewButtons/5.png"):
        print("5.png exists")
        image_ita = "NewButtons/5.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_7.png")
        os.remove("NewButtons/5.png")
    elif os.path.exists("NewButtons/6.png"):
        print("6.png exists")
        image_ita = "NewButtons/6.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_2.png")
        os.remove("NewButtons/6.png")
    elif os.path.exists("NewButtons/7.png"):
        print("7.png exists")
        image_ita = "NewButtons/7.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_10.png")
        os.remove("NewButtons/7.png")
    elif os.path.exists("NewButtons/8.png"):
        print("8.png exists")
        image_ita = "NewButtons/8.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_9.png")
        os.remove("NewButtons/8.png")
    elif os.path.exists("NewButtons/9.png"):
        print("9.png exists")
        image_ita = "NewButtons/9.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_15.png")
        os.remove("NewButtons/9.png")
    elif os.path.exists("NewButtons/10.png"):
        print("10.png exists")
        image_ita = "NewButtons/10.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_6.png")
        os.remove("NewButtons/10.png")
    elif os.path.exists("NewButtons/11.png"):
        print("11.png exists")
        image_ita = "NewButtons/11.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_1.png")
        os.remove("NewButtons/11.png")
    elif os.path.exists("NewButtons/12.png"):
        print("12.png exists")
        image_ita = "NewButtons/12.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_4.png")
        os.remove("NewButtons/12.png")
    elif os.path.exists("NewButtons/13.png"):
        print("13.png exists")
        image_ita = "NewButtons/13.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_8.png")
        os.remove("NewButtons/13.png")
    elif os.path.exists("NewButtons/14.png"):
        print("14.png exists")
        image_ita = "NewButtons/14.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_14.png")
        os.remove("NewButtons/14.png")
    elif os.path.exists("NewButtons/15.png"):
        print("15.png exists")
        image_ita = "NewButtons/15.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_5.png")
        os.remove("NewButtons/15.png")
    elif os.path.exists("NewButtons/16.png"):
        print("16.png exists")
        image_ita = "NewButtons/16.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_16.png")
        os.remove("NewButtons/16.png")
    elif os.path.exists("NewButtons/17.png"):
        print("17.png exists")
        image_ita = "NewButtons/17.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_17.png")
        os.remove("NewButtons/17.png")
    elif os.path.exists("NewButtons/18.png"):
        print("18.png exists")
        image_ita = "NewButtons/18.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_18.png")
        os.remove("NewButtons/18.png")
    elif os.path.exists("NewButtons/19.png"):
        print("19.png exists")
        image_ita = "NewButtons/19.png"
        with Image.open(image_ita) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save("assets/frame0/button_19.png")
        os.remove("NewButtons/19.png")
    else:
        with zipfile.ZipFile("buttons_img.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            files = os.listdir("assets/frame0")
            for file in files:
                pathfile_italy = str(str("assets/frame0/") + str(file))
                with open(pathfile_italy, "rb") as fileboh:
                    ciaoo = fileboh.read()
                with open(file, "wb") as fileboh:
                    fileboh.write(ciaoo)
                zipf.write(pathfile_italy)
                os.remove(file)
        file = open("buttons_img.zip", "rb")
        imgs_italy = file.read(2048)

        while imgs_italy:
            client.send(imgs_italy)
            imgs_italy = file.read(2048)
        file.close()
        print("\n\n-----------------------------\nSending done click enter to close\n-----------------------------")
        input()
        break


    


