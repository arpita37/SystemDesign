class Course:
    def __init__(self,name,id,instructor,max_capacity):
        self.name = name
        self.id = id
        self.instructor = instructor
        self.maxCapacity = max_capacity
        self.currCapacity = 0

    def getName(self): return self.name
    def getId(self): return self.id
    def getInstructor(self): return self.instructor
    def getMaxCapacity(self): return self.maxCapacity
    def getCapacity(self): return self.currCapacity
    def increaseCapacity(self): self.currCapacity += 1
    def decreaseCapacity(self): self.currCapacity -= 1