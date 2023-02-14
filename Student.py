from datetime import datetime

#Class Example
class Student:
    def __init__(self, firstname, lastname, birthdate, startdate):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.startdate = startdate


    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_birthdate(self):
        return self.birthdate

    def calculate_enddate(self):
        enddate = datetime(self.startdate)
        enddate = enddate
        self.enddate = enddate
        return self.enddate

    def getStudent(self):
        return self.firstname + " " + self.lastname

