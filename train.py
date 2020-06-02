import cv2
import numpy as np
from PIL import Image
import os
import pyttsx3

# Path for face image dataset
path = 'C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/HaarCascade/haarcascade_frontalface_default.xml")

# init functionis used to get an engine instance for the speech synthesis
engine = pyttsx3.init()
# function to get the all images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # to convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids
print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.yml') # we use recognizer.save()
# We Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
# the say method is used  for passing input text to be spoken 
engine.say('IMAGES TRAINED SUCCESSFULLY')
 # run and wait method, processes the voice commands.
engine.runAndWait()



