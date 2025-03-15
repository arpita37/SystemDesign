from Models.Spot.wheeler2Spot import ParkingSpotWheeler2
from Models.Spot.wheeler3Spot import ParkingSpotWheeler3
from Models.Spot.wheeler4Spot import ParkingSpotWheeler4
from Models.Spot.wheeler6Spot import ParkingSpotWheeler6
from Models.Vehicles.vehicle import Vehicle
from Models.Vehicles.wheeler2 import Wheeler2
from Models.Vehicles.wheeler3 import Wheeler3
from PublicInterfaces.parkingsystem import ParkingSystem
from Utils.SpotManager.wheeelr4Mgr import Wheeler4Mgr
from Utils.SpotManager.wheeler2Mgr import Wheeler2Mgr
from Utils.SpotManager.wheeler3Mgr import Wheeler3Mgr
from Utils.SpotManager.wheeler6Mgr import Wheeler6Mgr


class Demo:
    @staticmethod
    def run():
        spot2 = dict()
        spot3 = dict()
        spot4 = dict()
        spot6 = dict()
        for i in range(1,101):
            if i >0 and i<= 25:
                spot2[i] = ParkingSpotWheeler2(i,1)
                spot3[i] = ParkingSpotWheeler3(i+100, 1)
                spot4[i] = ParkingSpotWheeler4(i+200, 1)
                spot6[i] = ParkingSpotWheeler6(i+300, 1)
            elif i>25 and i<=50:
                spot2[i] = ParkingSpotWheeler2(i, 2)
                spot3[i] = ParkingSpotWheeler3(i + 100, 2)
                spot4[i] = ParkingSpotWheeler4(i + 200, 2)
                spot6[i] = ParkingSpotWheeler6(i + 300, 2)
            elif i>50 and i<= 75:
                spot2[i] = ParkingSpotWheeler2(i, 3)
                spot3[i] = ParkingSpotWheeler3(i + 100, 3)
                spot4[i] = ParkingSpotWheeler4(i + 200, 3)
                spot6[i] = ParkingSpotWheeler6(i + 300, 3)
            else:
                spot2[i] = ParkingSpotWheeler2(i, 4)
                spot3[i] = ParkingSpotWheeler3(i + 100, 4)
                spot4[i] = ParkingSpotWheeler4(i + 200, 4)
                spot6[i] = ParkingSpotWheeler6(i + 300, 4)

        w2 = Wheeler2Mgr(spot2)
        w3 = Wheeler3Mgr(spot3)
        w4 = Wheeler4Mgr(spot4)
        w6 = Wheeler6Mgr(spot6)

        pSObj = ParkingSystem(w2,w3,w4,w6)
        v1 = Wheeler2(1)
        pSObj.bookSpot(v1)
        v2 = Wheeler3(2)
        pSObj.bookSpot(v2)
        v3 = Wheeler2(3)
        pSObj.bookSpot(v3)
        v4 = Wheeler2(4)
        pSObj.bookSpot(v4)
        print(v1.getSpot().getId())
        pSObj.freeSpot(v2)
        vX = Wheeler3(10)
        pSObj.freeSpot(vX)

if __name__ == "__main__":
    Demo.run()