from Student import Student


class StudentManagement():
    def __init__(self, student):
        self.students = [student]

    def addStudent(self, student):
        self.students.append(student)

    def removeStudent(self, student):
        self.students.remove(self, student)

    def getStudents(self):
        for student in self.students:
            print(student.getStudent())

    def getNumberOfStudents(self):
        return self.students.copy()
