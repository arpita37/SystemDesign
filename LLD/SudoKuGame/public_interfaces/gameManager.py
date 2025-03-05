import logging
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Lock

from utils.board import Board
from utils.gameBoard import GameBoard
from utils.sudokuGame import SudokuGame


class GameManager:
    _instance = None
    _lock = ThreadPoolExecutor(max_workers=1)

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = super().__new__(cls)
                cls._instance.allBoard = Board()
                cls._instance.games = dict()
                cls._instance.log = logging.getLogger("GameManager")
        else:
            print("This is a singleton class")
        return cls._instance

    def createNewGame(self,name,players):
        self.log.info(f"Initializing new game with name {name}")
        newBoard = GameBoard(self.allBoard.getBoard())
        newGame = SudokuGame(name,newBoard,players)
        self.games[name] = newGame
        newGame.startGame()