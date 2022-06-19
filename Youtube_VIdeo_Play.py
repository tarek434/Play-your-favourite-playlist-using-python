import pywhatkit
import time
f = open("link.txt", "r")
y = f.readlines()
for i in y:
    pywhatkit.playonyt(i)
    print("Playing.....")
    time.sleep(20)
