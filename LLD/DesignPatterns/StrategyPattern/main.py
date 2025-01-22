from DesignPatterns.StrategyPattern.goodsVehicles import GoodsVehicle
from DesignPatterns.StrategyPattern.sportsVehicles import SportsVehicle


def main():
    goodsObj = GoodsVehicle()
    goodsObj.drive()

    sportsObj = SportsVehicle()
    sportsObj.drive()


if __name__ == "__main__":
    main()