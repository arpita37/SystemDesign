from threading import Lock
from typing import Set

from CoffeeTypes.coffeeInterface import CoffeeInterface
from Inventory.inventory import Inventory
from MachineStates.dispenseState import DispenseState
from MachineStates.idleState import IdleState
from MachineStates.readyState import ReadyState
from MachineStates.returnChangeState import ReturnChangeState


class CoffeeMachine:
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        with cls._lock:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = Inventory()
            cls._instance.menu : Set[CoffeeInterface] = set()
            cls._instance.selectedProduct = None
            cls._instance.idleState = IdleState(cls._instance)
            cls._instance.readyState = ReadyState(cls._instance)
            cls._instance.dispenseState = DispenseState(cls._instance)
            cls._instance.returnChangeState = ReturnChangeState(cls._instance)
            cls._instance.currentState = cls._instance.idleState
            cls._instance.totalPayemnt = 0.0
        return cls._instance

    @classmethod
    def getInstance(cls):
        if cls._instance:
            print("Already instantiated")
        return cls._instance

    def addToMenu(self, coffee : CoffeeInterface):
        for val in self.menu:
            if coffee.getName() == val.getName():
                self.menu.remove(val)
                break
        self.menu.add(coffee)
        print(f"\nCoffe type {coffee.getName()} added to the menu")

    def displayMenu(self):
        print("\nCOFFEETYPE\t\t\t\tPRICE")
        for pro in self.menu:
            print(f"\n{pro.getName()}\t\t\t{pro.getPrice()}")

    def setState(self, state):
        self.currentState = state

    def selectProduct(self, pro):
        self.currentState.selectProduct(pro)

    def addPayemnt(self, value : float):
        self.currentState.pay(value)

    def dispenseProduct(self):
        self.currentState.dispense()

    def returnChange(self):
        self.currentState.returnChange()
        self.reset_payment()
        self.reset_selected_product()

    def reset_payment(self):
        self.totalPayemnt = 0.0

    def reset_selected_product(self):
        self.selectedProduct = None


                
            
        
            