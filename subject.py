#import packages
import os
import time
#check date and subject
currentdate=time.strftime("%d_%m_%y")
subject=input("Enter Subject Name:")
a=['PGIS','SQA','ITSM','SIC','BI']
if subject in a:
    print("Success")
    os.startfile(r"C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/Attendance/"+subject+"/"+subject+currentdate+".xlsx")
else:
    print("Invalid")

