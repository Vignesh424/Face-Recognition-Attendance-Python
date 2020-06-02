#importing packages
from tkinter import*
import tkinter.messagebox
import os
#tkinter instance creation
master=Tk()
w = 415
h = 425
ws = master.winfo_screenwidth()
hs = master.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
master.geometry('%dx%d+%d+%d' % (w, h, x, y))
master.configure(background="#234567")
master.title("REGISTERATION DETAILS")

#Defining Functions
def  addition():
    master.destroy()
    os.system('py adduser.py')
    
def go():
    master.destroy()
    os.system('py lecture.py')

def back():
    master.destroy()
    os.system('py adminoptionwindow.py')

def close():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    master.destroy()
                         
    
#Create Buttons
Button(master, text='ENTER THE CREDENTIALS', command=addition ,font=("Times New Roman",20),fg="red",bg="#234567",height=2, cursor="sizing").grid(row=4, column=1, sticky=N+E+W+S, pady=10,padx=10)
Button(master, text='PROCEED FOR ATTENDANCE', command=go ,font=("Times New Roman",20),fg="red",bg="#234567",height=2,cursor="pirate").grid(row=5,column=1, sticky=N+E+W+S, pady=10,padx=10)
Button(master, text='BACK TO OPTION WINDOW', command=back ,font=("Times New Roman",20),fg="red",bg="#234567",height=2,cursor="pirate").grid(row=6,column=1, sticky=N+E+W+S, pady=10,padx=10)
Button(master, text='QUIT', command=close ,font=("Times New Roman",20),fg="red",bg="#234567",height=2,cursor="pirate").grid(row=7,column=1, sticky=N+E+W+S, pady=10,padx=10)
#End
master.mainloop()





