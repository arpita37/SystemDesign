class GameBoard:
    def __init__(self,board):
        self.board = board

    def showBoard(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j],end=" ")
            print("\n")


    def makeMove(self,r,c,val,log):
        if self.board[r][c] != 0:
            log.info(f"The cell {r},{c} is already occupied")
            return False

        self.board[r][c] = val
        log.info(f"Places {val} to cell ({r},{c})")
        return True


    def checkForWinner(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True