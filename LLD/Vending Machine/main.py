from PaymentTypes.coins import Coins
from Products.prouctsInterface import Product
from vendingMachine import VendingMachine


class VM:
    @staticmethod
    def run():
        print("\nInitializing product")
        coke = Product("Coke", 10)
        chips = Product("Chips", 20)
        chocolate = Product("Chocolate", 50)
        beer = Product("beer", 250)

        VM = VendingMachine().get_instance()
        VM.inventory.add_product(coke, 100)
        VM.inventory.add_product(chips, 100)
        VM.inventory.add_product(chocolate, 200)

        VM.inventory.getProductsList()

        VM.select_product(beer)
        VM.select_product(chips)
        VM.insert_coin(Coins.twenty)
        VM.dispense_product()


if __name__ == "__main__":
    VM.run()