from collections import deque
import time
from typing import List

from Models.dice import Dice
from Models.player import Player
from Utils.board import Board


class SnakeLadderGame:
    def __init__(self, p : List[Player]):
        self.dice = Dice()
        self.players = deque(p)
        self.board = Board()
        self.gameInitialized = False

    def initializeGame(self):
        print("\nInitializing Game!!!!")
        print(f"\nThere are {len(self.players)} players for this game!!")
        self.board.initializeGame()
        self.printBoard()

    def printBoard(self):
        print("\nCurrent players positions - ")
        print("\nPlyaerName\tPositions")
        for p in self.players:
            print(f"\n{p.getName()}\t{p.getPos()}")

    def rollDice(self):
        return self.dice.rollDice()

    def checkWinner(self, cell):
        if cell == 99:
            return True
        return False

    def startGame(self):
        self.initializeGame()
        winner = False
        while(not winner):
            player = self.players.popleft()
            print(f"{player.getName()} please roll the dice.")
            val = self.rollDice()
            if self.board.checkValidCell(player.getPos()+val):
                player.updatePos(val)
                cell = player.getPos()
                newCell = self.board.checkSnakeorLadder(cell)
                if newCell != 0:
                    player.resetPos(newCell)
                print(f"Diced roll with val {val}, current player {player.getName()}'s position is {player.getPos()}")
                winner = self.checkWinner(player.getPos())
                if winner:
                    print(f"\nThe winner of the game is {player.getName()}")
            self.players.append(player)