#import packages
import sqlite3
import os
from openpyxl import Workbook
import csv
import time

#check for the subjects
print(" 'SIC' , 'ITSM,'BI','PGIS','SQA' ")
subject=input("Enter Subject:")
lists=['BI','ITSM','SQA','SIC','PGIS']
if subject in lists:
    print("Success")
else:
    print("Failure")
a1=time.strftime("%d_%m_%y")
b2=str(time.strftime("%d_%m_%y"))
connect = sqlite3.connect("C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/sqlite3/Studentdb.db")
cursor = connect.cursor()
cursor.execute("SELECT * FROM Student")
rows = cursor.fetchall()
with open('report'+b2+'.csv', 'w') as f:
    a = csv.writer(f, delimiter=',')
    a.writerow(["ID","FULLNAME","EMAIL","ROLLNO","STATUS"])  ## etc
    a.writerows(rows)  ## closing paren added to the program
wb = Workbook()
ws = wb.active
ws.title='TYBSCIT'+subject
with open('report'+b2+'.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)


#check for the path
if os.path.exists('C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/REPORT/'+a1):
    wb.save('C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/Attendance/'+subject+"/"+subject+b2+'.xlsx')
else:
    os.path.exists('C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/REPORT/'+a1)
    wb.save('C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/Attendance/'+subject+"/"+subject+b2+'.xlsx')
       

       

#remove
os.remove("report"+b2+".csv")
print("done")
os.startfile("C:/Users/ACER/Desktop/PROJECT ALL RESOURCE/PROJECT ALL RESOURCE/Face recognition/Attendance/"+subject+"/"+subject+b2+'.xlsx')
