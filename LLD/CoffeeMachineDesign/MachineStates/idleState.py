from CoffeeTypes.coffeeInterface import CoffeeInterface
from MachineStates.machineStateInterface import MachineStates
from Products.product import Product

class IdleState(MachineStates):
    def __init__(self, cm):
        super().__init__(cm)

    def selectProduct(self, prod : CoffeeInterface):
        if not self.machine.inventory.checkAvailability(prod):
            print("\nThere isn't enough ingredients to make this coffee, please try selecting another type")
            return
        self.machine.selectedProduct = prod
        self.machine.setState(self.machine.readyState)

    def pay(self):
        print( "\nPlease select a coffee first to conitnue")

    def dispense(self):
        print( "\nPlease select a coffe and pay first to conitnue")

    def returnChange(self):
        print( "\nPlease select a coffee and pay first to conitnue")