from ParkingLotDesign.Vehicle.carVehicle import Car
from ParkingLotDesign.Vehicle.motorCycle import MotorCycle
from ParkingLotDesign.Vehicle.truck import Truck
from ParkingLotDesign.Vehicle.vehicleTypes import VehicleTypes
from ParkingLotDesign.parkingLot import ParkingLot


def main():
    parkingLotObj = ParkingLot()

    carObj1 = Car(10000, VehicleTypes.CAR.value)
    truckObj1 = Truck(12345, VehicleTypes.TRUCK.value)
    motorObj1 = MotorCycle(11231, VehicleTypes.MOTORCYCLE.value)

    parkingLotObj.parkVehicle(carObj1)
    parkingLotObj.parkVehicle(truckObj1)
    parkingLotObj.parkVehicle(motorObj1)

    carObj2 = Car(100001, VehicleTypes.CAR.value)
    truckObj2 = Truck(123451, VehicleTypes.TRUCK.value)
    motorObj2 = MotorCycle(112311, VehicleTypes.MOTORCYCLE.value)

    parkingLotObj.parkVehicle(carObj2)
    parkingLotObj.parkVehicle(truckObj2)
    parkingLotObj.parkVehicle(motorObj2)

    carObj2 = Car(1000011, VehicleTypes.CAR.value)
    parkingLotObj.parkVehicle(carObj2)

    parkingLotObj.unparkVehicle(truckObj2)

if __name__ == "__main__":
    main()