from collections import deque
from playing_piece_X import PlayingPieceX
from playing_piece_O import PlayingPieceO
from playing_piece_Y import PlayingPieceY
from player import Player
from board import Board

class TicTacToe:
    def __init__(self, no_of_players : int, boardSize:int) -> None:
        self.no_of_players = no_of_players
        self.boardSize = boardSize
        self.players = deque([])
        self.gameBoard = None
        self.initializeGame()


    def initializeGame(self):
        xPiece = PlayingPieceX()
        oPiece = PlayingPieceO()
        yPiece = PlayingPieceY()
        player1 = Player("Player1", xPiece)
        player2 = Player("Player2", oPiece)
        player3 = Player("Player3", yPiece )
        self.players.append(player1)
        self.players.append(player2)
        if self.no_of_players > 2:
            self.players.append(player3)
        self.gameBoard = Board(self.boardSize)
        print(f"Game initialization is done!")


    def startGame(self):
        noWinnerFound = True
        while(noWinnerFound):
            self.gameBoard.printBoard()
            freeSpace = self.gameBoard.getFreeSpace()
            if freeSpace == 0:
                print("The result is a tie")
                noWinnerFound = False
                continue
            playerTurn = self.players.popleft()
            print(f"Enter the row and column for player {playerTurn.getName()}")
            row,col = list(map(int, input().strip().split()))
            if not self.gameBoard.checkValidInput(row, col):
                print(f"Invalid row or column value, please try again")
                self.players.appendleft(playerTurn)
                continue
            self.gameBoard.addSymbol(row, col, playerTurn.piece.pieceType.value)
            isWinner = self.gameBoard.checkWinner(row,col,playerTurn.piece.pieceType.value)
            if isWinner:
                print(f"Winner of the game is {playerTurn.name}")
                noWinnerFound = False
                continue
            self.players.append(playerTurn)
