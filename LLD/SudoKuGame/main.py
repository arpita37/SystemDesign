from models.player import Player
from public_interfaces.gameManager import GameManager

class Demo:
    @staticmethod
    def run():
        mgrObj = GameManager()
        p1 = Player("Arpita",1)
        p2 = Player("Kingshuk",2)
        obj1 = mgrObj.createNewGame("Game1",[p1,p2])

if __name__ == "__main__":
    Demo.run()