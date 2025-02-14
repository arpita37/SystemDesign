import datetime
import uuid

class User:
    def __init__(self,name,contact):
        self.name = name
        self.id = self._generateUserId()
        self.contact = contact

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getContact(self):
        return self.contact

    def _generateUserId(self):
        return f"{uuid.uuid4().hex[:8]}_{datetime.datetime.today().strftime('%H_%m_%s')}"