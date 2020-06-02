#import module from tkinter and other packages
from tkinter import *
import os
import tkinter.messagebox

#creating instance of TK
root=Tk()
root.configure(background="#234567")
w = 440
h = 215
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.geometry("300x300")

#Defining Functions
def function1():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    root.destroy()

    
def attend():
    root.destroy()
    os.system('py subjectstudent.py')
    
#stting title for the window
root.title("ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
#creating a text label in tkinter
Label(root, text="**CHOOSE FROM THE OPTIONS**",font=("Times New Roman",20),fg="WHITE",bg="#1234ff",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating  buttons
Button(root,text="ATTENDANCE SHEET",font=("Times New Roman",20),bg="#234567",fg="red",command=attend,
cursor='man').grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="EXIT",font=("Times New Roman",20),bg="#234567",fg="red",command=function1,
cursor='cross').grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
#end
root.mainloop()
