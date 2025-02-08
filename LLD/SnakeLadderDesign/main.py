import time

from Models.player import Player
from Utils.gameEngine import GameEngine


class Demo:
    @staticmethod
    def run():
        obj = GameEngine()
        p1 = [Player("Arpita"),Player("Kingshuk"),Player("Alina")]
        obj.startNewGame(p1)
        time.sleep(10)
        p2 = [Player("Rajib"), Player("Patramita")]
        obj.startNewGame(p2)

if __name__ == "__main__":
    Demo.run()
