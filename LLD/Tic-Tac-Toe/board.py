class Board:
    def __init__(self, size:int) -> None:
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]


    def printBoard(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j],"|",end=" ")
            print("\n")

    def checkValidInput(self, row, col) -> bool:
        if row <0 or col < 0 or row >= self.size or col >= self.size or self.board[row][col] != " ":
            return False
        return True
    
    def getFreeSpace(self) -> None:
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    count += 1
        return count
    
    def addSymbol(self, row:int, col:int, sym) -> None:
        self.board[row][col] = sym


    def checkWinner(self, row, col, sym):
        first = second = third = fourth = True
        # Check for the row
        for i in range(self.size):
            if self.board[row][i] != sym:
                first = False

        # Check for the column
        for i in range(self.size):
            if self.board[i][col] != sym:
                second = False
        # Check for the left diagonal
        for i in range(self.size):
            if self.board[i][i] != sym:
                third = False

        # Check for the right diagonal
        for i in range(self.size):
            if self.board[self.size-i-1][self.size-i-1] != sym:
                fourth = False
        
        return first or second or third or fourth
        
        
        




