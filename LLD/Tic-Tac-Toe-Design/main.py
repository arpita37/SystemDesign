from Models.player import Player
from Models.playerPieceX import PlayerPieceX
from Models.playerPieceY import PlayerPieceY
from PublicInterfaces.gameController import GameController
from Utils.board import Board


class Demo:
    @staticmethod
    def run():
        ctrler = GameController()
        board = Board(3)
        pieceX = PlayerPieceX()
        pieceY = PlayerPieceY()
        p1 = Player(1,"Arpita",pieceX)
        p2 = Player(2,"Kingshuk", pieceY)
        ctrler.newGame(board,[p1,p2])

if __name__ == "__main__":
    Demo.run()