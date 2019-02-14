from random import randint

class Monster:
    hp = 1
    name = None

    def __init__(self, name):
        self.name = name

    def attackhit(self):
        """ Return True or False, if the monster's hit lands """
        if randint(0,1) == 1:
            return True
        return False

    def attackdamage(self):
        """ Determine the amount of damage an attack does. """
        return 1

class Kitten(Monster):
    hp = 10

    def __init__(self):
        super().__init__("kitten")

    def attackdamage(self):
        return randint(1,3)

class Tiger(Monster):
    hp = 30

    def __init__(self):
        super().__init__("tiger")

    def attackdamage(self):
        return randint(8,15)
