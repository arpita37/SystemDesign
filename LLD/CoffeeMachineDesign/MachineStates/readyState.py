from CoffeeTypes.coffeeInterface import CoffeeInterface
from MachineStates.machineStateInterface import MachineStates


class ReadyState(MachineStates):
    def __init__(self, cm):
        super().__init__(cm)

    def selectProduct(self, prod : CoffeeInterface):
        print( "Product already selected" )

    def pay(self, value : float):
        self.machine.totalValue += value
        if self.machine.totalValue < self.machine.selectedProduct.getPrice():
            print("Enter more ruppee , pyement is insufficient")
        else:
            self.machine.setState(self.machine.dispenseState)

    def dispense(self):
        print( "\nPlease select a coffee and pay first to conitnue")

    def returnChange(self):
        print( "\nPlease select a coffee and pay first to conitnue")