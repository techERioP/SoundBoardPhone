import os

filec = open("1.jpg", "rb")
pizza_migliore_su_tutto = filec.read()


file = open("2.jpg", "wb")
file.write(pizza_migliore_su_tutto)

