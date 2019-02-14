from player import Player
import game_locations


class Controller:
    player = None

    def start_game(self):
        print(" Welcome to the game!")
        print()
        name = input("What is your name? ")
        self.player = Player(name)
        self.player.move_to(game_locations.location_start)
        self.main_loop()

    def main_loop(self):
        exit = False

        while not exit:
            location = self.player.location

            # describe the current location
            print(location.long_description)

            if location.end:
                # end the game at an ending location
                print("Thank you for playing, {}!".format(self.player.name))
                break

            if location.monster:
                print("Oh no! There is a {} here!".format(
                    location.monster.name))
                self.fight(location)

                # if the player is at 0 hp after the fight, end the game
                if self.player.hp <= 0:
                    print("You have died.")
                    break

            print()
            print("You can go: ")
            options = list(location.paths)

            for index, option in enumerate(options):
                to_location = location.paths[option]
                print("{:>3} {} to {}".format(index + 1, option,
                                              to_location.short_description))

            print()
            choice = input("Your choice: ")
            try:
                choice = int(choice)

            except ValueError:
                print()
                print("\tERROR Improper input.")
                continue

            if choice < 1 or choice > len(options):
                print()
                print("\tERROR Improper input.")
                continue

            self.player.move_to(location.paths[options[choice - 1]])

    def fight(self, location):
        """ The player and the monster attack until one or the other is dead
        if the monster dies, it is removed from the location. """

        monster = location.monster

        while monster.hp > 0 and self.player.hp > 0:
            if monster.attackhit():
                print("The {} hits you!".format(monster.name))
                self.player.hp -= monster.attackdamage()
            else:
                print("The {} misses!".format(monster.name))

            if self.player.hp < 0:
                break

            print()
            print("You have {} HP and the monster has {}".format(
                self.player.hp, monster.hp))

            input("input anything to attack")
            if self.player.attackhit():
                print("You hit the {}!".format(monster.name))
                monster.hp -= self.player.attackdamage()
            else:
                print("You miss!")

            print()

        if monster.hp < 0:
            print("Congratulations! You have killed the {}! ".format(
                monster.name))
            location.remove_monster()


if __name__ == "__main__":
    c = Controller()
    c.start_game()
