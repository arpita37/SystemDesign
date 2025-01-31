from CoffeeTypes.coffeeInterface import CoffeeInterface
from Products.product import Product

class Inventory:
    def __init__(self):
        self._products : dict[Product] = dict()

    def disPlayProducts(self):
        print("\nPRODUCTNAME\t\t\t\tPRICE")
        for pro,val in self._products.items():
            print(f"\n{pro.getName()}\t\t\t{pro.getPrice()}")

    def addProduct(self, pro : Product, quantity : int):
        flag = False
        for p, q in self._products.items():
            if p.getName() == pro.getName():
                flag = True
                self._products[pro] += quantity
                break
        if not flag:
            self._products[pro] = quantity
        print(f"\nProduct {pro.getName()} added")

    def removeProduct(self, pro : Product, quantity : int):
        for key,val in self._products:
            if key.getName() == pro.getName():
                self._products[key] -= quantity


    def notify(self):
        for pro, val in self._products.items():
            if val <= 10:
                print(f"\nProduct {pro.getName()} has low quantity, add more!!!!!")


    def checkAvailability(self, coff : CoffeeInterface):
        items = coff.getIngredients()
        for pro,quant in items.items():
            for key, val in self._products.items():
                if key.getName() == pro and quant < val:
                    return False

        return True
