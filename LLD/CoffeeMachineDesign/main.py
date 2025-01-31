from CoffeeTypes.capuccino import Capuccino
from CoffeeTypes.espresso import Esprresso
from CoffeeTypes.lattee import Latte
from Machine.coffeMachine import CoffeeMachine
from Products.product import Product


class CoffeMachineDemo:
    @staticmethod
    def run():
        #Initialize machines
        machineObj = CoffeeMachine()
        machineObj.getInstance()

        #Add Ingredients to inventory
        sugar = Product("Sugar",50)
        milk = Product("Milk", 60)
        coffee = Product("Coffee", 350)

        machineObj.inventory.addProduct(sugar, 100)
        machineObj.inventory.addProduct(milk, 100)
        machineObj.inventory.addProduct(coffee, 100)

        #display products
        machineObj.inventory.disPlayProducts()

        #define coffee ingredients
        espresso = Esprresso({"Milk":2,"Sugar":1,"Coffee":2})
        latte = Latte({"Milk": 4, "Sugar": 2, "Coffee": 2})
        capuccino = Capuccino({"Milk": 3, "Sugar": 1, "Coffee": 3})
        machineObj.addToMenu(espresso)
        machineObj.addToMenu(latte)
        machineObj.addToMenu(capuccino)

        #display coffee menu
        machineObj.displayMenu()

        #select product
        machineObj.selectProduct(latte)

        #pay
        machineObj.addPayemnt(100)

        print(machineObj.totalPayemnt)

if __name__ == "__main__":
    CoffeMachineDemo.run()
