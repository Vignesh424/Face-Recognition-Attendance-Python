#we import module from tkinter for UI(User Interface)
from tkinter import *
import os
import tkinter.messagebox
    
#We are creating instance of TK with centering 
if __name__ == '__main__':
    root = Tk()
    root.title("ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
    w = 555
    h =615
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
root.geometry("%dx%d+%d+%d" %(w,h,x,y))
root.configure(background="#234567")

#Defining Functions
def function1():
    root.destroy()
    os.system("py admin.py")
    
def function2():
    root.destroy()
    os.system("py lecture.py")

def function3():
    root.destroy()
    os.system("py student.py")
    
def function4():
    tkinter.messagebox.askquestion("CONFIRMATION","ARE YOU SURE??")
    root.destroy()

#We are creating a text label
Label(root, text="***CHOOSE TO LOGIN FROM  OPTIONS***",font=("Times New Roman",20),fg="white",bg="#1234ff",height=2, compound=LEFT).grid(row=1,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)
photo1 = PhotoImage(file = r"C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Icons for Face recognition/admin.png")
photo2 = PhotoImage(file = r"C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Icons for Face recognition/lecture.png")
photo3 = PhotoImage(file = r"C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Icons for Face recognition/STUDS.png") 
photo4=  PhotoImage(file=r"C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Icons for Face recognition/clos.png")
# We are Resizing image to fit on button 
photoimage1 = photo1.subsample(5,5)
photoimage2 = photo2.subsample(5, 5)
photoimage3 = photo3.subsample(5, 5)
photoimage4 = photo4.subsample(5, 5)

#creating first button in tkinter
Button(root, text="ADMIN !", command=function1, font=("Times New Roman",20),bg="#234567",fg='red', image=photoimage1, compound=LEFT ,cursor='target').grid(row=3,columnspan=2,sticky=W+E+N+S,padx=10,pady=10)

#creating second button  in tkinter
Button(root,text="LECTURER !", command=function2, font=("Times New Roman",20),bg="#234567",fg='red', image=photoimage2, compound=LEFT , cursor='pirate').grid(row=4,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating third button  in tkinter
Button(root,text="STUDENT !",  command=function3, font=("Times New Roman",20), bg= "#234567",fg='red' , image=photoimage3, compound=LEFT, cursor='trek').grid(row=5,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating Exit button  in tkinter
Button(root,text="EXIT!",  command=function4, font=("Times New Roman",20), bg= "#234567",fg='red'  ,image=photoimage4, compound=LEFT, cursor='heart').grid(row=6,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)
root.mainloop()
