from Student import Student

#Inheritance Example
class WorkingStudent(Student):
    def __init__(self, firstname, lastname, birthdate, startdate, job):
        super().__init__(firstname, lastname, birthdate, startdate)
        self.job = job

    def getJob(self):
        return self.job

    #Override a inherit method
    def getStudent(self):
        return super().getStudent() + " " + self.birthdate



