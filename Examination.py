import csv
p=open("Examination.csv","w",newline='')
data=csv.writer(p)
data.writerow(["CourseName","StudentRollNumber","ExaminationMarks"])
for i in range (3):
    CourseName=input("CourseName")
    StudentRollNumber=input("StudentRollNumber")
    ExaminationMarks=int(input("ExaminationMarks"))
    info=[CourseName,StudentRollNumber,ExaminationMarks]
    data.writerow(info)
p.close()    