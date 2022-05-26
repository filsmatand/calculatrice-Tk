from cProfile import label
from cgitb import text
from distutils.cmd import Command
from mimetypes import common_types
from tkinter import *
from unittest import result

app=Tk()
app.geometry("250x300+1000+100")

nb1=""

def ajout(nb):
    global nb1
    nb1+=nb
    label["text"]=nb1

def num1():
    ajout("1")

def num2():
    ajout("2")

def num3():
    ajout("3")

def num4():
    ajout("4")
    
    
def num5():
    ajout("5")

def num6():
    ajout("6")
    
def num7():
    ajout("7")

def num8():
    ajout("8")
    
def num9():
    ajout("9")
    
def zero():
    ajout("0")
    
def ef():
    global nb1,nb2
    nb1=""
    nb2=""
    label["text"]=nb1    
    
def add():
    global nb1,op,nb2
    nb2=int(nb1)
    nb1=""
    op=1
    label["text"]="+"

    
def multi():
    global nb1,op,nb2
    nb2=int(nb1)
    nb1=""
    op=2
    label["text"]="x"
    
def sous():
    global  nb1,op,nb2
    nb2=int(nb1)
    nb1=""
    op=3
    label["text"]="-"
    
def div():
    global nb1,nb2,op
    nb2=int(nb1)
    nb1=""
    op=4
    label["text"]="%"
    
    
def egal():
    global nb1
    nb1=int(nb1)
    if(op==1):
        result=nb1+nb2
    if (op==2):
        result=nb1*nb2
    if (op==3):
        result =nb2-nb1
    if (op==4):
        result=nb2/nb1
        
    label["text"]=result
    nb1=int(result)
    
    
label=Label(app,text="0")
label.place(x=20,y=20)
button=Button(app,text="1" , command=num1).place(x=10,y=80)
button=Button(app,text="2" , command=num2).place(x=50,y=80)
button=Button(app,text="3" , command=num3).place(x=90,y=80)
button=Button(app,text="4" , command=num4).place(x=130,y=80)


button=Button(app,text="5", command=num5).place(x=10,y=120)
button=Button(app,text="6",command=num6).place(x=50,y=120)
button=Button(app,text="7",command=num7).place(x=90,y=120)
button=Button(app,text="8",command=num8).place(x=130,y=120)

button=Button(app,text="9",command=num9).place(x=10,y=160)
button=Button(app,text="0",command=zero).place(x=50,y=160)

button=Button(app,text="effacer",command=ef).place(x=90,y=160)

button=Button(app,text="+",command=add).place(x=10,y=200)
button=Button(app,text="x", command=multi).place(x=50,y=200)
button=Button(app,text="-",command=sous).place(x=90,y=200)
button=Button(app,text="%",command=div).place(x=130,y=200)



button=Button(app,text="=",command=egal).place(x=10,y=250)


app.mainloop()