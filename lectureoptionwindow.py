#import module from tkinter for UI and other packages
from tkinter import *
import tkinter.messagebox
import os

#creating instance of TK 
root = Tk()
root.title("ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
w = 470
h = 325
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(background="#234567")

#definition of function
def function1():
    root.destroy()
    os.system("py attendance.py")

def function2():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    root.destroy()

def function3():
    os.system("py subject.py")

    
#stting title for the window
root.title("OPTION WINDOW")

#creating a text label in tkinter
Label(root, text="***CHOOSE FROM THE OPTIONS***",font=("Times New Roman",20),fg="white",bg="#1234ff",
height=2).grid(row=0,rowspan=2,columnspan=2, sticky=N+E+W+S,padx=5,pady=5)

#creating first button  in tkinter
Button(root,text="ATTENDANCE",font=("Times New Roman",20),bg="#234567",fg='red',command=function1, compound=LEFT,
cursor='umbrella').grid(row=2,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating second button  in tkinter
Button(root,text="SUBJECT ATTENDANCE",font=("Times New Roman",20),bg="#234567",fg="red",command=function3, compound=LEFT,
cursor='spider').grid(row=4,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating third button  in tkinter
Button(root,text="EXIT",font=("Times New Roman",20),bg="#234567",fg="red",command=function2, compound=LEFT,
cursor='shuttle').grid(row=6,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

 #end
root.mainloop()
