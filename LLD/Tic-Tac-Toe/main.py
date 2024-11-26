from tictactoe import TicTacToe

def Main():
    print(f"Enter the number of players ( 2 or 3)")
    no_of_players = int(input())
    print(f"Enter the size of the board")
    size = int(input())
    game = TicTacToe(no_of_players, size)
    game.startGame()

Main()