from enum import Enum
class Paymentstatus(Enum):
    INITIATED : str = "INITIATED"
    PROGRESS : str = "PROGRESS"
    SUCCESSFUL : str = "SUCCESSFUL"
    CANCELLED : str = "CANCELLED"