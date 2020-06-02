#import packages
from tkinter import *
import os
import tkinter.messagebox
import sqlite3
import pyttsx3

#define functions
def login_user():
    #Check username and password entered are correct
    engine = pyttsx3.init()
    lists=['None']
    users=user.get()
    connects = sqlite3.connect("C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/sqlite3/Teachersdb.db")# connecting to the database
    c = connects.cursor()
    c.execute('SELECT USERNAME  FROM Teacher ORDER BY ID')
    rows=c.fetchall()
    for row in rows:
        lists.append('{0}'.format(row[0]))
    if users in lists:
        tkinter.messagebox.showinfo("VALIDATE", "VALIDATED SUCCESSFULLY")
        # say method on the engine that passing input text to be spoken
        engine.say('LECTURE LOGIN SUCCESSFULLY')
        # run and wait method, it processes the voice commands.
        engine.runAndWait()
        tkinter.messagebox.askokcancel("REDIRECT", "REDIRECTING YOU TO LECTURE OPTION PAGE")
        root.destroy()
        os.system("py lectureoptionwindow.py")
        connects.commit()# we are commiting into the database
        c.close()
        connects.close()# we are closing the connection
    else:
        # say method on the engine that passing input text to be spoken
        engine.say('LECTURE LOGIN FAILED, TRY AGAIN')
          # run and wait method, it processes the voice commands.
        engine.runAndWait()
        tkinter.messagebox.showerror("ERROR", "USERNAME OR ID INCORRECT")
        tkinter.messagebox.askretrycancel("WARNING", "TRY AGAIN")

        
        
        

def exits():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    root.destroy()

  #tkinter program  
root=Tk()
w = 630
h = 420
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
photo1 = PhotoImage(file = r"C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Icons for Face recognition/lecture.png")
photoimage1 = photo1.subsample(3,3)
Label(root, bg="#234567", image=photoimage1, cursor='pirate', compound=CENTER).grid(row=0,sticky=N+E+W+S, pady=5,padx=5)
root.title('LECTURE LOGIN SCREEN')
root.configure(background="#234567")
Label(text = ' USERNAME', font=("Times New Roman", 15),fg="red",bg="#234567",height=2).grid(row=1,sticky=N+E+W+S, pady=5,padx=5)
user= Entry(width="30", font=("Times New Roman",20),fg="white",bg="#234567", cursor="umbrella")
user.grid(row=1,column=2,sticky=N+E+W+S, pady=5,padx=5)
Button(text='LOGIN', command=login_user, font=("Times New Roman", 15),fg="red",bg="#234567",height=2, cursor="fleur").grid(row=2,column=2,sticky=N+E+W+S, pady=5,padx=5)
Button(text='EXIT', command=exits, font=("Times New Roman", 15),fg="red",bg="#234567",height=2, cursor="fleur").grid(row=3,column=2,sticky=N+E+W+S, pady=5,padx=5)
root.mainloop()






