class Product:
    def __init__(self, name : str, price : float):
        self._name = name
        self._price = price

    def getName(self):
        return self._name

    def getPrice(self):
        return self._price

    def changePrice(self, price: float):
        self._price = price