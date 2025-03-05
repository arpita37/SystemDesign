import copy
import random

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.allBoard = dict()
        self.counter = 0
        self.initalizeAllBoard()

    def removeFewCells(self,grid):
        grid[0][0] = 0
        grid[0][2] = 0
        grid[1][3] = 0
        grid[1][5] = 0
        grid[2][6] = 0
        grid[2][7] = 0

    def check(self,r, c, val):
        for i in range(9):
            if self.board[r][i] == val or self.board[i][c] == val or self.board[3 * (r // 3) + i // 3][3 * (c // 3) + (i % 3)] == val:
                return False
        return True

    def recursion(self):
        count = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    count += 1
                    for p in range(1, 10):
                        if self.check(i, j, p):
                            self.board[i][j] = p
                            if self.recursion():
                                return True
                            self.board[i][j] = 0
                    return False
        if count == 0:
            temp = copy.deepcopy(self.board)
            self.removeFewCells(temp)
            self.allBoard[self.counter] = temp
            self.counter += 1
        return True

    def initalizeAllBoard(self):
        for r in range(9):
            for i in range(1,10):
                self.board[r][0] = i
                self.recursion()
                self.board[r][0] = 0

    def getBoard(self):
        val = random.randint(0,self.counter)
        return self.allBoard[val]
