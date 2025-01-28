class Inventory:
    def __init__(self):
        self.products = dict()

    def add_product(self, name, quantity):
        self.products[name] = quantity

    def remove_product(self, name):
        del self.products[name]

    def __exists(self, name):
        for key,val in self.products.items():
            if key.getProductName() == name:
                return True
        return False

    def update_quantity(self, name, quantity):
        if not self.__exists(name):
            print( f"\nUnsuccessful operation. Product {name} doesn't exist in the inventory. Add it first!!!!")
            return
        for key, val in self.products.items():
            if key.getProductName() == name:
                self.products[key] = self.products.get(key,0)+quantity

    def remove_quantity(self,name,quantity):
        if self.__exists(name):
            print( f"\nUnsuccessful operation. Product {name} doesn't exist in the inventory. Add it first!!!!")
            return
        for key, val in self.products.items():
            if key.getProductName() == name:
                self.products[key] = self.products.get(key, 0) - quantity

    def isAvailable(self,name):
        for key,val in self.products.items():
            if key.getProductName() == name and val > 0:
                print( f"\nOnly {val} quantity is available for {name} product in inventory")
                return True
        return False

    def getProductsList(self):
        print( f"\nNAME\t\t\t\t\tPRICE\t\t\t\t\tQUANTITY")
        for key,val in self.products.items():
            print( f"\n{key.getProductName()}\t\t\t\t\t{key.getProductPrice()}\t\t\t\t\t{val}")