class Contract:
    def __init__(self, id, room, checkin, checkout, user):
        self.id = id
        self.room = room
        self.checkin = checkin
        self.checkout = checkout
        self.user = user

    def getContractId(self): return self.id
    def getRoom(self): return self.room
    def getCheckinDate(self): return self.checkin
    def getCheckoutDate(self): return self.checkout
    def getUser(self): return self.user
    def updateCheckinDate(self,d1):
        self.checkin = d1
        self.room.updateCheckin(d1)
    def updateCheckoutDate(self, d1):
        self.checkout = d1
        self.room.updateCheckout(d1)
