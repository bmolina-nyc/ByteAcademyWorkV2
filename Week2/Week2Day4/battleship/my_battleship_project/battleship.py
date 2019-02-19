from gameboard import Gameboard
from player import Player

MISS = "M"
HIT = "X"
SHIP = "S"
BLANK = " "

class Game:
    def __init__(self):
        
        #initialize the players
        print("Player 1 - Please enter your name")
        name1 = input()
        print()
        print("Player 2 - Please enter your name")
        name2 = input()
        print()
        self.player1, self.player2 = Player(name1), Player(name2)
        while True:
            print("Please enter the size of the game grid. From 4 to 12")
            grid_size = input()
            if grid_size.isdigit() != True or int(grid_size) not in range(4,12):
                print()
                print("Invalid size")
                continue
            else:
                break

        gameboard = Gameboard(grid_size)

        while True:
            if gameboard.win():
                last_turn = gameboard.game_turn() - 1
                if last_turn % 2 != 0:
                    print(f"{self.player1.name} wins!")
                else:
                    print(f"{self.player2.name} wins!")
                break

            if  gameboard.game_turn() % 2 != 0:
                gameboard.display_own_board(self.player1.name)
                gameboard.display_opponent_board()
                print(f"{self.player1.name} take your turn")
                move = self.player1.place_mark()
                gameboard.place_mark(move, self.player1.name)
                
            else:
                gameboard.display_own_board(self.player2.name)
                gameboard.display_opponent_board()
                print(f"{self.player2.name} take your turn")
                move = self.player2.place_mark()
                gameboard.place_mark(move, self.player2.name)

def run():
    Game()

if __name__ == "__main__":
    run()