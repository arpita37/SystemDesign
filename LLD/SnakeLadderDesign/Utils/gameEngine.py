import threading
from collections import defaultdict
from PublicInterface.snakeLadderGame import SnakeLadderGame


class GameEngine:
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        self.games = defaultdict()
        self.count = 0

    @staticmethod
    def getInstance(self):
        if not self._instance:
            with self._lock:
                if not self._instance:
                    self._instance = GameEngine()
        return self._instance

    def startNewGame(self, playerNames):
        with self._lock:
            self.count += 1
            game = SnakeLadderGame(playerNames)
            self.games[self.count] = game
            threading.Thread(target=game.startGame).start()