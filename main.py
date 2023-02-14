from Student import Student
from StudentManagement import StudentManagement
from WorkingStudent import WorkingStudent

erik = Student("erik", "test", "11.10.1990", "01.09.2023")
def printStudentsName():
    print(erik.get_firstname())

def printEnddate():
    return erik.calculate_enddate()

def printJob():
    amanda = WorkingStudent("test", "mei", "11.19.2000", "01.01.2023", "devops eng")
    print(amanda.getJob())
printStudentsName()
printJob()

tim = WorkingStudent("tim", "tam", "11.19.2000", "01.01.2023", "devops eng")
print(tim.getStudent())

students = StudentManagement(tim)
students.addStudent(erik)
print(students.getStudents())