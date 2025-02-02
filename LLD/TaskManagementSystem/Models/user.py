import random
from datetime import datetime

class User:
    def __init__(self, name: str, email : str):
        self.name = name
        self.email = email
        self.id = random.randint(0,10000000)
        self.creationDate = datetime.today().strftime("%Y-%m-%d %H-%M-%S")

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getId(self):
        return self.id

    def getCreationDate(self):
        return self.creationDate

    def notifyUser(self, msg, id=None):
        if id != None:
            id = id
        print(msg)
