from random import randint

class Monster():
    def __init__(self, name="",  weapon=""):
        self.name = name 
        self.health = 50
        self.weapon = weapon

    def attack(self):
        pass

    def damage(self):
        pass

class Beast(Monster):
    def __init__(self):
        super().__init__("Beast", "Claws")

class Witch(Monster):
    def __init__(self):
        super().__init__("Witch", "Potion")

class Gargoyle(Monster):
    def __init__(self):
        super().__init__("Gargoyle", "Fangs")
 
class Demon(Monster):
    def __init__(self):
        super().__init__("Demon", "Fire")

