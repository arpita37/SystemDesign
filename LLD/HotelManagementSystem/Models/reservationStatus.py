from enum import Enum

class ReservationStatus(Enum):
    AVIALABLE : str = "Available"
    OCCUPIED : str = "Occupied"
    RESERVED : str = "Reserved"