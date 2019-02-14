import game_locations
from random import randint

class Player:
    hp = 100
    name = None
    location = None

    def __init__(self, name):
        self.name = name

    def move_to(self, location):
        """ Change the current location to another """
        self.location = location

    def attackhit(self):
        """ Determine if the player's attack hits """
        if randint(0, 1) == 1:
            return True

    def attackdamage(self):
        """ Determine how much damage the player's attack hits """
        return randint(1, 6) + randint(1, 6)
