from MachineStates.machineStatesInterface import MachineStates
from PaymentTypes.coins import Coins
from PaymentTypes.notes import Notes
from Products.prouctsInterface import Product

class IdleState(MachineStates):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product) -> bool:
        if not self.vending_machine.inventory.isAvailable(product.getProductName()):
            print( f"\nThis product is not available at the inventory, please select another product")
            return False # to be implemented in main class
        self.vending_machine.selectedProduct = product
        self.vending_machine.set_state(self.vending_machine.readyState)
        return True

    def insert_coin(self,coin:Coins):
        print( f"\nPlease select a product first")

    def insert_note(self, note:Notes):
        print( f"\nPlease select a product first")

    def dispense_product(self):
        print( f"\nPlease select a product and make payment")

    def return_change(self):
        print( f"\nNothing to return")