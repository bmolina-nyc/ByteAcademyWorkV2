class Player():
    def __init__(self, name):
        self.name = name

    def place_mark(self):
        row = input("What row would you like to choose? ") 
        column = input("What column would you like to choose? ")
        print()
        return (str(row),str(column))