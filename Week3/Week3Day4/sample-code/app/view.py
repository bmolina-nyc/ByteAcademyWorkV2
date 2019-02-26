def welcome_screen():
    print("Welcome to Terminal Trader!")
    print()
    print("Choose your selection: ")
    print("Please enter 1, 2 or 3:")
    print("1 - Create account")
    print("2 - Log in")
    print("3 - Quit")

def main_menu():
    print("1. see balance & positions")
    print("2. deposit money")
    print("3. look up stock price")
    print("4. buy stock")    
    print("5. sell stock")
    print("6. trade history")

def get_input():
    print()
    print("Your choice: ", end="")
    return input()