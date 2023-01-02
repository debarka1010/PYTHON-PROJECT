import csv
p=open("Student.csv","w",newline='')
data=csv.writer(p)
data.writerow(["StudentID","Name","ClassRollNumber","BatchID"])
for i in range (4):
    StudentID=input("EnterStudentID")
    Name=input("EnterName")
    ClassRollNumber=int(input("EnterClassRollNumber"))
    BatchID=input("EnterBatchID")
    info=[StudentID,Name,ClassRollNumber,BatchID]
    data.writerow(info)
p.close()