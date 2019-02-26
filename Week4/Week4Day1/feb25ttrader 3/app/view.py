class View():

    def welcome_screen(self):
        print("Welcome to Terminal Trader!")
        print()
        print("Please make a selection - choose 1, 2, or 3")
        print()
        print("1. create account")
        print("2. login")
        print("3. quit")
        print()
        return input()

    def get_username(self):
        print()
        print("Please enter a username:", end="")
        print()
        return input()

    def add_balance(self):
        print()
        print("How much would you like to add to your account?", end="")
        print()
        return input()

    def get_password(self):
        print() 
        print("Please enter a password", end="")
        print()
        return input()

    def confirm_password(self):
        print()
        print("Please confirm your password", end="")
        print()
        return input()

    def improper_password(self):
        print()
        print("Passwords do not match! Please try again")
        print()

    def improper_balance(self):
        print()
        print("Balance is invalid - please enter only a numeric positive value")
        print()

    def goodbye(self):
        print()
        print("Thank you - Goodbye!")
        print()

    def logged_in_screen(self, username, balance):
        print()
        print(f"Hello {username}")
        print(f"Your current balance is {balance}")
        print()
        print("Please select from the following options:")
        print()

        