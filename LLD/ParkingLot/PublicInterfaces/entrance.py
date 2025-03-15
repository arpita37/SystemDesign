import datetime
import uuid

from dateutil.utils import today

from Models.Vehicles.vehicleTypes import VehicleTypes
from Models.ticket import Ticket
from Utils.SpotManager.parkingSpotManager import ParkingspotManager


class EntraceGate:
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

    def BookSpot(self,vh):
        obj: ParkingspotManager = self.PMgrFactory(vh)
        sp = obj.findSpot()
        if not sp:
            return None
        vh.setSpot(obj.spotList[sp])
        obj.parkVehicle(sp,vh)
        self.generateTicket(obj.spotList[sp],vh)
        return obj.spotList[sp]

    def generateTicket(self,sp,vh):
        txnId = self.generateId()
        tick = Ticket(txnId,datetime.datetime.now(),vh,sp)
        vh.setTicket(tick)

    def generateId(self):
        return f"{uuid.uuid4().hex[:8]}_{datetime.datetime.now().strftime('%MM-%YY')}"
