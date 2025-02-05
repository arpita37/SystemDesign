from Models.pieceType import PieceType


class Board:
    def __init__(self, dim):
        self.dim = dim
        self.board = [["_" for i in range(dim)] for _ in range(dim)]

    def printBoard(self):
        for row in range(self.dim):
            for col in range(self.dim):
                print(self.board[row][col], end= " ")
            print("\n")

    def getFreeSpace(self):
        count = 0
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] == "_":
                    count += 1
        return count > 0

    def checkWinner(self, r,c,piece : PieceType):
        #check row
        flag = True
        for col in range(self.dim):
            if self.board[r][col] != piece.value:
                flag = False
        if flag:
            return True

        #check column
        flag = True
        for row in range(self.dim):
            if self.board[row][c] != piece.value:
                flag = False
        if flag:
            return True

        #check (0,0)-(n-1,n-1) diagonal
        r,c = self.dim-1, self.dim-1
        flag = True
        while r>=0 and c >=0:
            if self.board[r][c] != piece.value:
                flag = False
            r -= 1
            c -= 1

        if flag:
            return True

        #check (n-1,0)-(0,n-1) diagonal
        flag = True
        r,c = self.dim-1, 0
        while(r >=0 and c <= self.dim):
            if self.board[r][c] != piece.value:
                flag = False
            r -= 1
            c += 1

        return flag

    def checkAvailability(self, r,c):
        return self.board[r][c] == "_"

    def placePiece(self, r, c, piece : PieceType):
        self.board[r][c] = piece.value
