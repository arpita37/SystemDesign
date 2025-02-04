import random


class User:
    def __init__(self, name  :str, contact : str, license=None):
        self.id = random.randint(0,1000000)
        self.name = name
        self.contactDetail = contact
        self.contract = None
        self.license = license

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getContractDetail(self):
        return self.contactDetail

    def setContractDetail(self, con):
        self.contactDetail = con

    def getLicense(self):
        return self.license