from enum import Enum

#Can be extended as per requirement, follow's Liskov's Substitution Principle
class PieceTypes(Enum):
    X : str = 'X'
    Y : str = 'Y'