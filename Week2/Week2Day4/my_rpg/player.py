from random import randint

class Player():
    def __init__(self, name="Hero"):
        self.name = name 
        self.health = 100
        self.weapon = ""


    def attack(self):
        return randint(1, 10)


    def damage(self):
        return randint(1, 10)


