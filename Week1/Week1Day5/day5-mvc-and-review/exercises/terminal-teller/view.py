def show_homepage():
    print("Welcome to Terminal Teller! Please select 1, 2 or 3:")
    print()
    print("1) create account")
    print("2) log in")
    print("3) quit")

def homepage_input():
    print()
    print("Your choice: ", end="")
    print()
    return input()
 
def get_first_name():
        print("First Name: ", end="")
        return input()

def get_last_name():
    print("Last Name: ", end="")
    return input()

def get_pin():
    print("Enter PIN: ", end="")
    return input()

def confirm_pin():
    print("confirm PIN: ", end="")    
    return input()

def create_account():
    first = get_first_name()
    last =  get_last_name()
    pin = get_pin()
    confirmed_pin = confirm_pin()
    return [first, last, pin, confirmed_pin]

def logged_in_main_menu():
    print("main menu")