from pprint import pprint
from random import randint

MISS = "M"
HIT = "X"
SHIP = "S"
BLANK = " "

class Gameboard:
    def __init__(self, gridsize, p1_boards = [[],[]], p2_boards = [[],[]], turn = 1):
        self.p1_boards = p1_boards
        self.p2_boards = p2_boards
        self.turn = turn
        self.p1_hp = 1
        self.p2_hp = 1
        self.gridsize = int(gridsize)

        for _ in range(self.gridsize):
            row = []
            for _ in range(self.gridsize):
                row.append(BLANK)
            self.p1_boards[0].append(row.copy())
            self.p1_boards[1].append(row.copy())
            self.p2_boards[0].append(row.copy())
            self.p2_boards[1].append(row.copy())
        self.p1_boards[0][randint(0,self.gridsize-1)][randint(0,self.gridsize-1)] = SHIP
        self.p2_boards[0][randint(0,self.gridsize-1)][randint(0,self.gridsize-1)] = SHIP

    
    def game_turn(self):
        return self.turn 

    def test_display(self):
        print(list(range(1, len(self.p1_boards[0])+1)))
        for row in self.p1_boards[0]:
            print(row)

    def display_own_board(self, name):
        print()
        print(f"{name} - this is your board")
        if self.game_turn() % 2 != 0:
            pprint(self.p1_boards[0])
            print()
        else:
            pprint(self.p2_boards[0])
            print()

    def display_opponent_board(self):
        print("This is your oppenents board")
        if self.game_turn() % 2 != 0:
            pprint(self.p1_boards[1])
            print()
        else:
            pprint(self.p2_boards[1])
            print()

    def win(self):
        if self.p1_hp == 0:
            return True 
        elif self.p2_hp == 0:
            return True
        else:
            return False 
        
    # this needs to be updated to note the specific gameboard that is being updated for hits or misses
    def place_mark(self, tup, name):
        x,y = tup
        # validation - checks for integers that are in range of the board size and for numbers
        if x.isdigit() != True or y.isdigit() != True or int(x) not in range(1, len(self.p1_boards[0])+1) or int(y) not in range(1,len(self.p1_boards[0])+1):
            print(f"Invalid move - {name} Please try again!")
            return False 

        x,y = int(x)-1, int(y)-1
        if self.game_turn() % 2 != 0:
            if self.p2_boards[0][x][y] == BLANK:
                print("That is a miss")
                self.p1_boards[1][x][y] = MISS
            elif self.p2_boards[0][x][y] == SHIP:
                print("Direct Hit!")
                self.p1_boards[1][x][y] = SHIP
                self.p2_hp -= 1
        elif self.game_turn() % 2 == 0:
            if self.p1_boards[0][x][y] == BLANK:
                print("That is a miss")
                self.p2_boards[1][x][y] = MISS
            elif self.p1_boards[0][x][y] == SHIP:
                print("Direct Hit!")
                self.p2_boards[1][x][y] = SHIP
                self.p1_hp -= 1

        self.turn += 1

  
