# selinin zeka oyunu
from tkinter import *
import random
import time
#from gtts import gTTS
import os

puan = 0
ofof = ["",""]
started = 0

def nextt():

    global started
    started += 1
    btn.config(text="Next")
    btn.pack()

    global puan
    global ofof

    game_yz = ["black","pink","red","white","yellow","green","blue","purple","orange"]
    a = random.randint(0, 8)
    a = game_yz[a]
    a = a.lower()
    ofof.append(a)
    """try:
        tts = gTTS(text='{}'.format(a))
        tts.save("merhaba.mp3")
        os.system("merhaba.mp3")
    except:
        print("İnternet bağlantınız olmadığı için hata oluştu.")"""

    if a == "black" or a == "BLACK":
        text1.config(bg="white")
    else:
        text1.config(bg="black")


    a = a.lower()
    cvp = ent.get()
    cvp = cvp.upper()
    cvp = cvp.replace("i","ı")
    cvp = cvp.replace("İ","I")

    if started > 1:
        cevap = ofof[-2]
        cevap = cevap.upper()
        cevap = cevap.replace("i","ı")
        cevap = cevap.replace("İ","I")

        if cevap == cvp:

            puan += 1
            print(cevap,"==",cvp)
            kontrol.config(text="True!\nScore: {}".format(puan),bg="green",fg="black")
            kontrol.pack()
        else:
            puan -= 1
            print(cevap, "==", cvp)
            kontrol.config(text="False!\nScore: {}".format(puan),bg="red",fg="black")
            kontrol.pack()
    else:
        pass

    a = a.upper()
    text1.config(text=">> {} <<".format(a), fg="{}".format(a))
    text1.pack()







def rot():
    root = Tk()
    root.title("COLOR GAME")
    root.geometry("500x500")
    root.resizable(0,0)
    root.config(bg="pink")

    yazi1 = "\nDeveloper: Mertcan Balcı\n11.08.2020\n\n"
    text = Label()

    text.config(text="{}".format(yazi1),bg="pink",fg="black",font=("Calibri",16))
    text.pack()
    global text1
    a = 0
    text1 = Label()
    text1.config(text="{}".format("Ready!"),fg="white",bg="{}".format("black"),font=("Calibri",32))
    text1.pack()

    bos = Label()
    bos.config(bg="pink",fg="pink",font=("Calibri",13))
    bos.pack()
    global ent
    ent = Entry()
    ent.config(font=("Calibri",25))
    ent.pack()

    bos2 = Label()
    bos2.config(bg="pink", fg="pink", font=("Calibri", 13))
    bos2.pack()



    global btn
    btn = Button()
    btn.config(text="Start!",bg="black",font=("Calibri",21),fg="white",command=nextt)
    btn.pack()

    bos3 = Label()
    bos3.config(bg="pink", fg="pink", font=("Calibri", 13))
    bos3.pack()

    global kontrol
    kontrol = Label()
    kontrol.config(text="{} Score: {}".format("Lets Go !",puan),fg="white",bg="black",font=("Calibri",23))
    kontrol.pack()

    root.mainloop()


rot()
