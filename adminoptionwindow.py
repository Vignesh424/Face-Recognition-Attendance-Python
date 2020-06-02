#import module from tkinter for UI and import other needed packages
from tkinter import *
import os
from datetime import datetime
import sqlite3 as sq
import tkinter.messagebox

#creating instance of TK 
root = Tk()
root.title("ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
w = 550
h = 525
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(background="#234567")
con1 = sq.connect('C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/sqlite3/Studentdb.db')
con2 = sq.connect('C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/sqlite3/Teachersdb.db') 
c1 = con1.cursor()
c2=con2.cursor()

#define functions
def function1():
    root.destroy()
    os.system("py studentregister.py")

def function2():
    root.destroy()
    os.system("py addteacher.py")

def exit():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    root.destroy()

def function3():
    os.startfile("C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/dataset/")

def registered_names():
    c1.execute('SELECT ID,FULLNAME,EMAIL,ROLLNO FROM Student')
    for (ID, FULLNAME,EMAIL, ROLLNO) in c1:
        print("ID:{},FULLNAME:{},EMAIL:{},ROLLNO:{}".format(ID,FULLNAME,EMAIL,ROLLNO))
    print("Done")
    con1.commit()
    con1.close()

def registered_names2():
    c2.execute('SELECT * FROM Teacher')
    for (ID,NAME, USERNAME) in c2:
        print("ID:{},NAME:{}, USERNAME:{}".format(ID,NAME, USERNAME))
    print("Done")
    con2.commit()
    con2.close()

#setting title for the window
root.title("OPTION WINDOW")

#creating a text label in tkinter
Label(root, text="***CHOOSE FROM THE OPTIONS***",font=("Times New Roman",20),fg="white",bg="#1234ff",
height=2).grid(row=0,rowspan=2,columnspan=2, sticky=N+E+W+S,padx=5,pady=5)

#creating first button  in tkinter
Button(root,text="REGISTER STUDENT",font=("Times New Roman",20),bg="#234567",fg='red',command=function1, compound=LEFT,
cursor='umbrella').grid(row=2,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating first button  in tkinter
Button(root,text="REGISTER TEACHERS",font=("Times New Roman",20),bg="#234567",fg='red',command=function2, compound=LEFT,
cursor='umbrella').grid(row=3,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating third button  in tkinter
Button(root,text="VIEW REGISTERED USERS IMAGES",font=("Times New Roman",20), bg= "#234567",fg='red',command=function3, compound=LEFT,
cursor='pirate').grid(row=4,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating fourth button  in tkinter
Button(root,text="VIEW REGISTERED RECORDS",font=("Times New Roman",20),bg="#234567",fg="red",command=registered_names, compound=LEFT,
cursor='spider').grid(row=5,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating  fifth button  in tkinter
Button(root,text="VIEW REGISTERED TEACHER RECORDS",font=("Times New Roman",20),bg="#234567",fg="red",command=registered_names2, compound=LEFT,
cursor='spider').grid(row=6,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating  exit button  in tkinter
Button(root,text="EXIT",font=("Times New Roman",20),bg="#234567",fg="red",command=exit, compound=LEFT,
cursor='shuttle').grid(row=7,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

root.mainloop()
