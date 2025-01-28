from threading import Lock
from Inventory.inventory import Inventory
from MachineStates.dispenseState import DispenseState
from MachineStates.idleState import IdleState
from MachineStates.machineStatesInterface import MachineStates
from MachineStates.readyState import ReadyState
from MachineStates.returnChangeState import ReturnChangeState
from PaymentTypes.coins import Coins
from PaymentTypes.notes import Notes
from Products.prouctsInterface import Product


class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = Inventory()
            cls._instance.idleState = IdleState(cls._instance)
            cls._instance.readyState = ReadyState(cls._instance)
            cls._instance.dispenseState = DispenseState(cls._instance)
            cls._instance.returnChangeState = ReturnChangeState(cls._instance)
            cls._instance.selectedProduct = None
            cls._instance.current_state = cls._instance.idleState
            cls._instance.total_payment = 0.0
        return cls._instance

    classmethod
    def get_instance(cls):
        return cls._instance

    def select_product(self, product: Product):
        self.current_state.select_product(product)

    def insert_coin(self, coin: Coins):
        self.current_state.insert_coin(coin)

    def insert_note(self, note: Notes):
        self.current_state.insert_note(note)

    def dispense_product(self):
        self.current_state.dispense_product()

    def return_change(self):
        self.current_state.return_change()

    def set_state(self, state: MachineStates):
        self.current_state = state

    def add_coin(self, coin: Coins):
        self.total_payment += coin.value

    def add_note(self, note: Notes):
        self.total_payment += note.value

    def reset_payment(self):
        self.total_payment = 0.0

    def reset_selected_product(self):
        self.selected_product = None