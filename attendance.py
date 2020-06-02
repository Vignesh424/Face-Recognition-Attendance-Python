#import packages
from tkinter import*
import tkinter.messagebox
import os

#creating instance of TK 
root = Tk()
w = 447
h = 470

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(background="#234567")

#defining functions
def function1():
    os.system("py train.py")

def function2():
    os.system('py facedetect.py')

def exits():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    root.destroy()

def function3():
    os.system("py landmarks.py")

def function4():
    os.system("py recognize.py")

def function5():
    os.system("py database.py")




#stting title for the window
root.title("ATTENDANCE WINDOW")
#creating a text label in tkinter
Label(root, text="ATTENDANCE MARKING SYSTEM",font=("Times New Roman",20),fg="white",bg="#1234ff",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating buttons in tkinter
Button(root,text="TRAINING",font=("Times New Roman",20),bg="#234567",fg="red",command=function1,
cursor='heart').grid(row=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="FACE DETECTION",font=("Times New Roman",20),bg="#234567",fg="red",command=function2,
cursor='shuttle').grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="FACE LANDMARKS",font=("Times New Roman",20),bg="#234567",fg="red",command=function3,
cursor='spider').grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="RECOGNIZE",font=("Times New Roman",20),bg="#234567",fg="red",command=function4,
cursor='man').grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="ATTENDANCE",font=("Times New Roman",20),bg="#234567",fg="red",command=function5,
cursor='man').grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="EXIT",font=("Times New Roman",20),bg="#234567",fg="red",command=exits,
cursor='pirate').grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#end
root.mainloop()
