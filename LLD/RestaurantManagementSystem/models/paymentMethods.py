from enum import Enum

class PaymentMethod(Enum):
    CASH : str = "CASH"
    CARD  :str = "CARD"
    UPI : str = "UPI"