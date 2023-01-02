import csv
p=open("Batch.csv","w",newline='')
data=csv.writer(p)
data.writerow(["BatchID","BatchName","DepertmentName","LifeofCourse","ListofStudent"])
for i in range (3):
    BatchID=input("EnterBatchID")
    BatchName=input("EnterBatchName")
    DepartmentName=input("EnterDepartmentName")
    ListofCourse=input("EnterListofCourse")
    ListofStudent=input("EnterListofStudent")
    info=[BatchID,BatchName,DepartmentName,ListofCourse,ListofStudent]
    data.writerow(info)
p.close()