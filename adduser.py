import cv2
import os
import sqlite3
import dlib
import re,time
from playsound import playsound
import pyttsx3 
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier('C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/HaarCascade/haarcascade_frontalface_default.xml')
detector = dlib.get_frontal_face_detector()
# init function to get an engine instance for the speech synthesis  
engine1 = pyttsx3.init()
engine2 = pyttsx3.init() 
# For each person, enter one numeric face id
detector = dlib.get_frontal_face_detector()
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
Id =int(input("Enter ID:"))
fullname = input("Enter FullName : ")
email=input("Enter Email:")
match = re.match(regex,email)
if match == None:
    print('Invalid Email')
    raise ValueError('Invalid Email')
rollno = int(input("Enter Roll Number : "))
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# say method on the engine that passing input text to be spoken 
playsound('sound.mp3')
engine1.say('User Added Successfully')
# run and wait method, it processes the voice commands.  
engine2.runAndWait() 
connects = sqlite3.connect("C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/sqlite3/Studentdb.db")# connecting to the database
c = connects.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Student (ID INT NOT NULL UNIQUE PRIMARY KEY, FULLNAME TEXT NOT NULL, EMAIL NOT NULL, ROLLNO INT UNIQUE NOT NULL , STATUS TEXT DATE TIMESTAMP)')
c.execute("INSERT INTO Student(ID, FULLNAME, EMAIL,ROLLNO) VALUES(?,?,?,?)",(Id,fullname,email,rollno))
print('Record entered successfully')
connects.commit()# commiting into the database
c.close()
connects.close()# closing the connection
# Initialize individual sampling face count
count = 0
while(True):
    ret, img = cam.read()
    img = cv2.flip(img,1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(Id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
        playsound('sound.mp3')
        engine2.say('DataSets Captured Successfully')
        # run and wait method, it processes the voice commands.
        engine2.runAndWait()
        break
# Doing a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
