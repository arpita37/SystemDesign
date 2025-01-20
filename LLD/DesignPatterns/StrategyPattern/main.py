from DesignPatterns.StrategyPattern.goodsVehicles import GoodsVehicle
from DesignPatterns.StrategyPattern.sportsVehicles import SportsVehicle


def main():
    goodsObj = GoodsVehicle()
    goodsObj.Drive()

    sportsObj = SportsVehicle()
    sportsObj.Drive()


if __name__ == "__main__":
    main()