class Staff:
    def __init__(self,id,name,role,contact):
        self.id = id
        self.name  =name
        self.role = role
        self.contact = contact
        self.rating = 0.0

    def getId(self): return self.id
    def getName(self): return self.name
    def getRole(self): return self.role
    def getContact(self): return self.contact
    def getRating(self): return self.rating
    def updateRating(self,rating): self.rating += rating