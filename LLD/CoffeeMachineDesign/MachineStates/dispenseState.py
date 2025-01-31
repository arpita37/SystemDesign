from CoffeeTypes.coffeeInterface import CoffeeInterface
from MachineStates.machineStateInterface import MachineStates


class DispenseState(MachineStates):
    def __init__(self, cm):
        super().__init__(cm)

    def selectProduct(self, prod : CoffeeInterface):
        print( "\nProduct already selected")

    def pay(self):
        print("\nProduct selected, payment done")

    def dispense(self):
        items = self.machine.selectedProduct.getIngredients()
        for pro, quant in items.items():
            self.machine.inventory.removeProduct( pro, quant )

    def returnChange(self):
        print( "\nPlease select a coffee and pay first to conitnue")