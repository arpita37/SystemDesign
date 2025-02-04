import threading

class Dispenser:
    def __init__(self, amount):
        self.available_amount = amount
        self.lock = threading.Lock()

    def dispense_Cash(self, amount):
        with self.lock:
            if amount > self.available_amount:
                print("Available balance is not sufficient to perform this operation")
                return False
            self.available_amount -= amount
            return True