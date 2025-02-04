class Card:
    def __init__(self, number : str, pin : int):
        self.cardNo = number
        self.pin = pin

    def getCardNo(self):
        return self.cardNo

    def getPin(self):
        return self.pin

    def resetPin(self, pin: int):
        self.pin = pin