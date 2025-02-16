class Reservation:
    def __init__(self,id,name, contact, size,time):
        self.id = id
        self.name = name
        self.contact = contact
        self.size = size
        self.bookingTime = time

    def getId(self): return self.id
    def getName(self): return self.name
    def getContact(self): return self.contact
    def getSize(self): return self.size
    def getTime(self): return self.bookingTime