#importing packages
from tkinter import *
import os
import tkinter.messagebox
import re,pyttsx3

#Define functions
def login_user():
    #Check username and password entered are correct
    # init function to get an engine instance for the speech synthesis
    engine=pyttsx3.init()
    user= 'student@sies.in'
    password ='student@123'
    if use.get() == user and passw.get() == password:
        tkinter.messagebox.showinfo("STUDENT LOGIN", "STUDENTLOGIN SUCCESSFULLY")
        # say method on the engine that passing input text to be spoken 
        engine.say('STUDENT LOGIN SUCCESSFULLY')
        # run and wait method, it processes the voice commands.
        engine.runAndWait() 
        tkinter.messagebox.askokcancel("REDIRECT", "REDIRECTING YOU TO STUDENT ACCESS PAGE")
        root.destroy()
        os.system("py studentaccess.py")
    else:
        '''Prompt user that either id or password is wrong'''
        tkinter.messagebox.showerror("ERROR", "USERNAME OR PASSWORD INCORRECT")
        tkinter.messagebox.askretrycancel("WARNING", "TRY AGAIN")


def exits():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    root.destroy()


 #tkinter   
root=Tk()
w = 630
h = 450
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
 #tkinter photo adding to label
photo1 = PhotoImage(file = r"C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Icons for Face recognition/STUDS.png")
photoimage1 = photo1.subsample(3,3)
 #tkinter  label
Label(root, bg="#234567", image=photoimage1, cursor='pirate', compound=CENTER).grid(row=0,sticky=N+E+W+S, pady=5,padx=5)
root.title('STUDENT LOGIN SCREEN')
root.configure(background="#234567")
 #tkinter  label
Label(text = ' USERNAME ', font=("Times New Roman", 15),fg="red",bg="#234567",height=2).grid(row=1,sticky=N+E+W+S, pady=5,padx=5)
Label(text = ' PASSWORD', font=("Times New Roman", 15),fg="red",bg="#234567",height=2).grid(row=2,sticky=N+E+W+S, pady=5,padx=5)
 #tkinter  Entry box
use=Entry(width="30",font=("Times New Roman",20),fg="white",bg="#234567", cursor="umbrella")
use.grid(row=1,column=2,sticky=N+E+W+S, pady=5,padx=5)
 #tkinter  Entry box
passw= Entry(show='*', width="30", font=("Times New Roman",20),fg="white",bg="#234567", cursor="umbrella")
passw.grid(row=2,column=2,sticky=N+E+W+S, pady=5,padx=5)
 #tkinter  Buttons
Button(text='LOGIN', command=login_user, font=("Times New Roman", 15),fg="red",bg="#234567",height=2, cursor="fleur").grid(row=3, column=2,sticky=N+E+W+S, pady=5,padx=5)
Button(text='EXIT', command=exits, font=("Times New Roman", 15),fg="red",bg="#234567",height=2, cursor="fleur").grid(row=4, column=2,sticky=N+E+W+S, pady=5,padx=5)
#End
root.mainloop()






