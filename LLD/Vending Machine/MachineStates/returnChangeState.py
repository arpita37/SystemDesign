from MachineStates.machineStatesInterface import MachineStates
from PaymentTypes.coins import Coins
from PaymentTypes.notes import Notes
from Products.prouctsInterface import Product

class ReturnChangeState(MachineStates):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product):
        print("\nProduct already selected")

    def insert_coin(self, coin:Coins):
        print("\nPayment already done")

    def insert_note(self, note: Notes):
        print("\nPayment already done")

    def dispense_product(self):
        print(f"\nProduct {self.vending_machine.selectedProduct.getProductName} already dispensed")

    def return_change(self):
        if self.vending_machine.total_payment >= self.vending_machine.selectedProduct.getProductPrice():
            rem = self.vending_machine.total_payment - self.vending_machine.selectedProduct.getProductPrice()
            print(f"Returned change of {rem} ruppee")
        self.vending_machine.reset_selected_product()
        self.vending_machine.set_state(self.vending_machine.idleState)