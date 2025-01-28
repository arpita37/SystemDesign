from MachineStates.machineStatesInterface import MachineStates
from PaymentTypes.coins import Coins
from PaymentTypes.notes import Notes
from Products.prouctsInterface import Product


class ReadyState(MachineStates):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product : Product):
        print( "\nProduct already selected")

    def insert_coin(self, coin : Coins):
        self.vending_machine.add_coin(coin)
        print( f"\nCoin inserted {coin.name}")
        self.check_payment_status()


    def insert_note(self, note : Notes):
        self.vending_machine.add_coin(note)
        print(f"\nNote inserted {note.name}")
        self.check_payment_status()

    def dispense_product(self):
        print( f"\nPlease make payemnt for selected product")


    def return_change(self):
        print(f"\nNothing to return")

    def check_payment_status(self):
        if self.vending_machine.total_payment >= self.vending_machine.selectedProduct.getProductPrice():
            self.vending_machine.set_state(self.vending_machine.dispenseState)
        else:
            price = self.vending_machine.selectedProduct.getProductPrice()
            print(f"\n{self.vending_machine.total_payment} is less than product price {price}")
