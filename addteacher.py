#Import Packages
from tkinter import *
import os
import tkinter.messagebox
import sqlite3
import pyttsx3

# init function is used to get an engine instance for the speech synthesis  
engine = pyttsx3.init()

def testVal1(inStr,i,acttyp):
    ind=int(i)
    if acttyp == '1': #insert validation
        if not inStr[ind].isdigit():
            return False
    return True


def testVal2(inStr,i,acttyp):
    ind=int(i)
    if acttyp == '1': #insert validation
        if not inStr[ind].isalpha():
            return False
    return True

def regis_user():
    Id=ids.get()
    name=names.get()
    user=uses.get()
    connects = sqlite3.connect("C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/sqlite3/Teachersdb.db")
    # connecting to the database Teacherdb
    c = connects.cursor()
    c.execute("INSERT INTO Teacher VALUES(?,?,?)", (Id, name,user))
    connects.commit()# we are commiting into the database
    tkinter.messagebox.showinfo("ADD TEACHER", "ADDED TECHER SUCCESSFULLY")
    # the say method is used on the engine that passing input text to be spoken
    engine.say('Teacher Added Successfully')
    # we use run and wait method, it processes the voice commands.
    engine.runAndWait() 
    tkinter.messagebox.askokcancel("REDIRECT", "REDIRECTING YOU TO LECTURE LOGIN PAGE")
    root.destroy()
    os.system("py lecture.py")
    c.close()
    connects.close()# the closing of the connection


def exits():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    root.destroy()


    
root=Tk()
w = 650
h = 525
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
photo1 = PhotoImage(file = r"C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Icons for Face recognition/Lecture.png")
photoimage1 = photo1.subsample(3,3)
Label(root, bg="#234567", image=photoimage1, cursor='pirate', compound=CENTER).grid(row=0,sticky=N+E+W+S, pady=5,padx=5)
root.title('TEACHER REGISTER')
root.configure(background="#234567")
Label(text = ' ID', font=("Times New Roman", 15),fg="red",bg="#234567",height=2).grid(row=1,sticky=N+E+W+S, pady=5,padx=5)
Label(text = ' NAME ', font=("Times New Roman", 15),fg="red",bg="#234567",height=2).grid(row=2,sticky=N+E+W+S, pady=5,padx=5)
Label(text = ' USERNAME', font=("Times New Roman", 15),fg="red",bg="#234567",height=2).grid(row=3,sticky=N+E+W+S, pady=5,padx=5)

ids=Entry(width="30",font=("Times New Roman",20),fg="white",bg="#234567", cursor="umbrella", validate="key")
ids['validatecommand'] = (ids.register(testVal1),'%P','%i','%d')
ids.grid(row=1,column=2,sticky=N+E+W+S, pady=5,padx=5)

names=Entry(width="30",font=("Times New Roman",20),fg="white",bg="#234567", cursor="umbrella", validate="key")
names['validatecommand'] = (names.register(testVal2),'%P','%i','%d')
names.grid(row=2,column=2,sticky=N+E+W+S, pady=5,padx=5)

uses=Entry(width="30",font=("Times New Roman",20),fg="white",bg="#234567", cursor="umbrella")
uses.grid(row=3,column=2,sticky=N+E+W+S, pady=5,padx=5)



Button(root,text="REGISTER!",  command=regis_user, font=("Times New Roman",15), bg= "#234567",fg='red' , height=2,   cursor='trek').grid(row=4, column=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="EXIT",  command=exits, font=("Times New Roman",15), bg= "#234567",fg='red' ,height=2, cursor='trek').grid(row=5, column=2,sticky=N+E+W+S,padx=5,pady=5)
root.mainloop()






