import logging
import time

logging.basicConfig(level=logging.INFO)
from collections import deque
from threading import Lock

from Models.player import Player


class GameManager:
    def __init__(self,board,players,name):
        self.board = board
        self.players : deque[Player] = deque(players)
        self.name = name
        self.log = logging.getLogger(name)
        self.lock = Lock()

    def initializeGame(self):
        self.log.info(f"Initializing game {self.name}")
        self.log.info(f"The board looks like - ")
        self.board.showBoard()

    def startGame(self):
        winnerFound = False
        self.log.info("Starting the game")
        with self.lock:
            while(not winnerFound):
                self.board.showBoard()
                p = self.players.popleft()
                self.log.info(f"Player {p.getName()} please enter the row and column, separated by space")
                r,c = list(map(int,input().strip().split(" ")))
                if not self.board.validateCell(r,c):
                    self.log.warning("The cell is already occupied, please enter another one")
                    self.players.appendleft(p)
                    continue

                self.board.placePiece(p.getPiece().getPieceType().value,r,c)
                self.players.append(p)
                if self.board.findWinner(p.getPiece().getPieceType().value,r,c):
                    self.log.info(f"The winner is {p.getName()}")
                    winnerFound = True
        self.log.info("Game is done!!!!")
