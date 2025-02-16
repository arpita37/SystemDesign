from enum import Enum
class Status(Enum):
    PENDING : str = "PENDING"
    PREPARING : str=  "PREPARING"
    READY  :str = "READY"
    COMPLETED : str = "COMPLETED"
    CANCELLED : str = "CANCELLED"