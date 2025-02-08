from Models.ladder import Ladder
from Models.snake import Snake

class Board:
    def __init__(self):
        self.cells = [[None for _ in range(10)] for _ in range(10)]

    def initializeGame(self):
        # Initialize snakes
        self.cells[0][3] = Snake(3,0)
        self.cells[1][6] = Snake(16, 6)
        self.cells[4][8] = Snake(48, 26)
        self.cells[6][4] = Snake(64, 60)
        self.cells[9][3] = Snake(93, 73)

        # Initialize ladders
        self.cells[0][1] = Ladder(1, 38)
        self.cells[0][4] = Ladder(4, 14)
        self.cells[0][9] = Ladder(9, 31)
        self.cells[2][1] = Ladder(21, 42)
        self.cells[2][8] = Ladder(28, 84)
        self.cells[5][1] = Ladder(51, 67)
        self.cells[8][0] = Ladder(80, 99)

    def checkValidCell(self,cell):
        r = cell // 10
        c = cell % 10
        if r >= 10 or r < 0 or c >= 10 or c < 0:
            return False
        return True

    def checkSnakeorLadder(self,cell):
        val = 0
        if not self.checkValidCell(cell):
            return val
        r = cell//10
        c = cell%10
        obj = self.cells[r][c]
        if isinstance(obj,Snake) or isinstance(obj,Ladder):
            val = obj.getEnd()
        return val