class Student:
    def __init__(self,id,name,contact):
        self.name = name
        self.id = id
        self.contact = contact
        self.courses = dict()


    def getName(self): return self.id
    def getId(self): return self.id
    def getContact(self): return self.contact
    def addCourseID(self,id,course): self.courses[id] = course
    def courseExists(self,id):
        for val in self.courses.values():
            cID = val.getId()
            if id == cID:
                return True
        return False