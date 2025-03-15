import logging
import time

logging.basicConfig(level=logging.INFO)
from threading import Lock
from Utils.gameManager import GameManager
from queue import Queue

class GameController:
    _instance = None
    _lock = Lock()
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = super().__new__(cls)
                cls._instance.games = Queue()
                cls._instance.counter = 0
                cls._instance.log = logging.getLogger()
        else:
            print("This is a singleton class!!!!")

        return cls._instance

    def newGame(self,board,players):
        gameObj = GameManager(board,players,f"Game_{self.counter}")
        self.games.put(gameObj)
        self.playGame(gameObj)

    def playGame(self,game):
        game.initializeGame()
        time.sleep(1)
        game.startGame()