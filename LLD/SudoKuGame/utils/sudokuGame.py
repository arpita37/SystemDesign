import logging
from collections import deque
from utils.gameBoard import GameBoard
from threading import Lock
logging.basicConfig(level=logging.INFO)

class SudokuGame:
    def __init__(self,name,board,players):
        self.name : str = name
        self.board : GameBoard= board
        self.players  = deque(players)
        self.log = logging.getLogger(f"{self.name}")
        self.lock = Lock()

    def showBoard(self):
        self.board.showBoard()

    def startGame(self):
        winnerfound = False
        self.log.info("Starting the game")
        while(not winnerfound):
            self.showBoard()
            p = self.players.popleft()
            r,c,val = list(map(int,input(f"\n{p.getName()}, please enter your turn").strip().split(" ")))
            with self.lock:
                val = self.board.makeMove(r,c,val,self.log)
                if not val:
                    self.players.appendleft(p)
                    continue
                if self.board.checkForWinner():
                    self.log.info(f"Winner of the game is {p.getName()}")
                    return
                self.players.append(p)
