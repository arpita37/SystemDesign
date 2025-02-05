from PublicInterfaces.board import Board
import logging
from collections import deque
logging.basicConfig(level=logging.INFO)

class TicTacToeGame:
    def __init__(self, dim, p1, p2):
        self.board = Board(dim)
        self.player1 = p1
        self.player2 = p2
        self.log = logging.getLogger("Tic-Tac-Toe")
        self._initiateGame()

    def _initiateGame(self):
        self.log.info(f"Player1 has the piece {self.player1.getPiece()}")
        self.log.info(f"Player2 has the piece {self.player2.getPiece()}")
        self.log.info(f"Please enter the row and column separated by a space")


    def startGame(self):
        winnerFound = False
        q = deque([self.player1, self.player2])
        while(not winnerFound):
            self.board.printBoard()
            player = q.popleft()
            self.log.info(f"Player {player.getName()}'s turn,\n please enter row and column for piecetype {player.getPiece()}")
            r,c = map(int,input().strip().split(" "))
            res = self.board.checkAvailability(r,c)
            if not res:
                self.log.warning(f"Invalid cell entry, cell already filled")
                q.appendleft(player)
                continue
            self.board.placePiece(r,c,player.getPiece())
            winnerFound = self.board.checkWinner(r,c,player.getPiece())
            if not winnerFound:
                c = self.board.getFreeSpace()
                if c == 0:
                    self.log.info(f"The game is a draw\n------THE END----------")
                    winnerFound = True

            if winnerFound:
                self.board.printBoard()
                self.log.info(f"The winner of the game is {player.getName()}\n------THE END----------")
            q.append(player)

