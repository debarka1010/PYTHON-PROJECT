import csv
p=open("Courseproj.csv","w",newline='')
data=csv.writer(p)
data.writerow(["CourseID","CourseName","Marksobtained"])
for i in range (2):
    CourseID=input("EnterCourseID")
    CourseName=input("EnterCourseName")
    Marksobtained=input("Enter MarksOtained")
    info=[CourseID,CourseName,Marksobtained]
    data.writerow(info)
p.close()