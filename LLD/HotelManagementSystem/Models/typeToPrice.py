from Models.roomTypes import Roomtype

class TypeToPrice:
    @staticmethod
    def getPrice(type : Roomtype):
        match type:
            case Roomtype.SINGLE:
                return 2000
            case Roomtype.DOUBLE:
                return 3500
            case Roomtype.DELUXE:
                return 4500
            case Roomtype.SUITE:
                return 7000