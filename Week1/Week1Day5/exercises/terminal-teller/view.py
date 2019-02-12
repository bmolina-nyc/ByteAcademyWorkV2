def show_homepage():
    print()
    print("Welcome to Terminal Teller!:")
    print()
    print("Please enter 1, 2 or 3:")
    print("1 - Create account")
    print("2 - Log in")
    print("3 - Quit")

def get_input():
    print()
    print("Your choice: ", end="")
    return input()

def get_first_name():
    print("Enter your first name: ", end="")
    print()
    return input()

def get_last_name():
    print("Enter your last name: ", end="")
    print()
    return input()

def get_pin():
    print("Enter your pin: ", end="")
    print()
    return input()

def confirm_pin():
    print("Confirm your pin: ", end="")
    print()
    return input()

def login_name():
    print("Please enter your Full Name: ", end="")
    print()
    return input()

def login_pin():
    print("Please enter your PIN: ", end="")
    print()
    return input()

def logged_in_homepage(customer):
    print()
    print(f"Hello - {customer['Name']}")
    print("How can we help you today?")
    print()
    print("1) Check balance")
    print("2) Withdraw funds")
    print("3) Deposit funds")
    print("4) Sign out")
