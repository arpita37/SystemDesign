from Models.player import Player
from PublicInterfaces.tictactoe import TicTacToeGame
from Utils.playerPieceO import PlayerPieceO
from Utils.playerPieceX import PlayerPieceX


def main():
    print("How many dimentional game do you want?")
    n = int(input())
    player1 = Player("Arpita",PlayerPieceX())
    player2 = Player("kingshuk",PlayerPieceO())
    gameObj = TicTacToeGame(n,player1, player2)
    gameObj.startGame()

if __name__ == "__main__":
    main()