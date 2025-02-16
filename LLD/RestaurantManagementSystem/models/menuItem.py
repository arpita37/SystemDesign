class Menuitem:
    def __init__(self,id,name,description,price,availability):
        self.id = id
        self.name = name
        self.desc = description
        self.price = price
        self.availability = availability

    def getId(self): return self.id
    def getName(self): return self.name
    def getDesc(self): return self.desc
    def getPrice(self): return self.price
    def is_available(self): return  self.availability
    def updateAvailibilty(self,val): self.availability = val
    def updatePrice(self,val): self.price = val