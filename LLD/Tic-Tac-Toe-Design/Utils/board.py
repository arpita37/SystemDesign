class Board:
    def __init__(self,size):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]

    def showBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j],end="|")
            print("\n")

    def findWinner(self,sym,row,col):
        flag = True
        for i in range(self.size):
            if self.board[row][i] != sym:
                flag = False
                break
        if flag:
            return flag

        flag = True
        for i in range(self.size):
            if self.board[i][col] != sym:
                flag = False
                break
        if flag:
            return flag

        flag = True
        r,c = 0,0
        while(r<self.size and c<self.size):
            if self.board[r][c] != sym:
                flag = False
                break
            r += 1
            c += 1

        if flag:
            return flag

        flag = True
        r, c = 0,self.size-1
        while (r < self.size and c >= 0):
            if self.board[r][c] != sym:
                flag = False
                break
            r += 1
            c -= 1

        return flag


    def validateCell(self,row,col):
        if self.board[row][col] != " ":
            return False
        return True

    def placePiece(self,sym,row,col):
        self.board[row][col] = sym