from MachineStates.machineStatesInterface import MachineStates
from PaymentTypes.coins import Coins
from PaymentTypes.notes import Notes
from Products.prouctsInterface import Product


class DispenseState(MachineStates):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product):
        print( "\nProduct already selected")

    def insert_coin(self,coin:Coins):
        print("\nPayment already done")

    def insert_note(self, note:Notes):
        print("\nPayment already done")

    def dispense_product(self):
        product = self.vending_machine.selectedProduct
        self.vending_machine.inventory.update_quantity(product.name, 1)
        print(f"Product dispensed: {product.name}")
        self.vending_machine.set_state(self.vending_machine.returnChangeState)

    def return_change(self):
        pass