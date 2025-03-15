from Models.Vehicles.vehicleTypes import VehicleTypes
from Utils.Costing.costCalculator import CostCalculator
from Utils.Costing.w2Calc import w2Calculator
from Utils.Costing.w3Calc import w3Calculator
from Utils.Costing.w4Calc import w4Calculator
from Utils.Costing.w6Calc import w6Calculator
from Utils.SpotManager.parkingSpotManager import ParkingspotManager


class ExitGate:
    def __init__(self,w2,w3,w4,w6):
        self.wheel2Mgr = w2
        self.wheel3Mgr = w3
        self.wheel4Mgr = w4
        self.wheel6Mgr = w6

    def PMgrFactory(self,vh):
        vhtype = vh.getType()
        match vhtype:
            case VehicleTypes.WheelerType2:
                return self.wheel2Mgr
            case VehicleTypes.WheelerType3:
                return self.wheel3Mgr
            case VehicleTypes.WheelerType4:
                return self.wheel4Mgr
            case VehicleTypes.WheelerType6:
                return self.wheel6Mgr
            case _:
                return self.wheel6Mgr

    def CostMgrFactory(self,vh):
        vhtype = vh.getType()
        match vhtype:
            case VehicleTypes.WheelerType2:
                return w2Calculator()
            case VehicleTypes.WheelerType3:
                return w3Calculator()
            case VehicleTypes.WheelerType4:
                return w4Calculator()
            case VehicleTypes.WheelerType6:
                return w6Calculator()
            case _:
                return CostCalculator()


    def freeSpot(self,vh):
        obj: ParkingspotManager = self.PMgrFactory(vh)
        obj.unparkVehicle(vh.getTicket().getSpot().getId())

    def calculatePrice(self,vh):
        ccObj = self.CostMgrFactory(vh)
        return ccObj.calculate(vh.getTicket().getSpot().getPrice(),vh.getTicket().getEntrytime())