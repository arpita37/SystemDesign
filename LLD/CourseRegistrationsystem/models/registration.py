import datetime

class Registration:
    def __init__(self, id,student, course):
        self.id = id
        self.student = student
        self.course = course
        self.registration_time = datetime.datetime.today()

    def getId(self): return self.id
    def getStudent(self): return self.student
    def gteCourse(self): return self.course