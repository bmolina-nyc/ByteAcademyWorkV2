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
    print(f"Hello - {customer[0][0]} - Acct.No: {customer[0][1]}")
    print(f"Your balance is currently {customer[0][3]}")
    print()
    print("How can we help you today?")
    print()
    print("1) Withdraw funds")
    print("2) Deposit funds")
    print("3) Sign out")

def withdraw_funds():
    print()
    print("How much would you like to withdraw?: ")
    return input()

def deposit_funds():
    print()
    print("How much would you like to deposit?: ")
    return input()

def insufficient_funds():
    print()
    print("You have insufficient funds please try again")

def invalid_amount():
    print()
    print("Please enter a whole number amount")

def bad_selection():
    print()
    print("Try again! - Enter correct number value only")

def no_pin_match():
    print()
    print("Pins do not match, please try again")
    print()

def invalid_login():
    print()
    print("Invalid Login - please try again")
    print()

def goodbye():
    print()
    print("Goodbye!")

