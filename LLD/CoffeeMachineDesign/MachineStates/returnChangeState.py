from CoffeeTypes.coffeeInterface import CoffeeInterface
from MachineStates.machineStateInterface import MachineStates


class ReturnChangeState(MachineStates):
    def __init__(self, cm):
        super().__init__(cm)

    def selectProduct(self, prod : CoffeeInterface):
        print( "Product already selected" )

    def pay(self, value : float):
        self.machine.addPayemnt(value)

    def dispense(self):
        print( "\nPlease select a coffee and pay first to conitnue")

    def returnChange(self):
        if self.machine.totalPayemnt >= self.machine.selectedProduct.getPrice():
            print( f"Change of Rs. {self.machine.totalPayemnt - self.machine.selectedProduct.getPrice()}")
        self.machine.setState(self.machine.idleState)