#function define

def printTeachers(teachers):
    for i in range(0,numberOfTeachers):
        print("teacher ",i," name is ",teachers[i])


def showSchoolDetails(teachers):
    print("school name is ",schoolName)
    print("number of students are ",numberOfStudents)
    print("number of teachers are ",numberOfTeachers)
    printTeachers(teachers)


schoolName = "ABC School"

numberOfStudents = int(input("Enter the number of students: "))
numberOfTeachers = int(input("Enter the number of teachers: "))

print("Enter all the Teachers name : ")
teachers = []  #array list

for i in range(0,numberOfTeachers):
    print("enter ",i," teacher name")
    teacherName = input()
    teachers.append(teacherName)


i=0;
showSchoolDetails(teachers)









