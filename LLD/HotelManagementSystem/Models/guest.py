class Guest:
    def __init__(self, id, name, contactType, contactInfo):
        self.name = name
        self.id = id
        self.contactType = contactType
        self.contact = contactInfo
        self.room = None

    def getNanem(self): return self.name
    def getId(self): return self.id
    def getContactType(self): return self.contactType
    def getContact(self): return self.contact
    def getRoom(self): return self.room