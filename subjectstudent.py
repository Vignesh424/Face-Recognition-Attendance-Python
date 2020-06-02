#import packages
import os
import time
import pandas as pd
#CHECK SUBJECT AND TIME
currentdate=time.strftime("%d_%m_%y")
subject=input("Enter Subject Name:")
a=['PGIS','SQA','ITSM','SIC','BI']
if subject in a:
    print("Success")
    sample_file=pd.read_excel('C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/Attendance/'+subject+"/"+subject+currentdate+'.xlsx', sheet_name="TYBSCIT"+subject)
    print(sample_file)
    print()
    input("Press Enter To Exit:")
else:
    print("Invalid")
    print()
    input("Press Enter To Exit:")

