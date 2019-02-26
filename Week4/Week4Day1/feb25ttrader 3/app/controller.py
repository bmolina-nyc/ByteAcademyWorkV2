from app.account import Account
from app.view import View 

view = View()

def run():
    welcome_homepage()


def welcome_homepage():
    while True:  
        selection = view.welcome_screen()


        if selection == "1":
            username, balance, password, confirm_password = view.get_username(), view.add_balance(), view.get_password(), view.confirm_password()
            
            if password != confirm_password:
                view.improper_password()
                continue  
            if not balance.isdigit() or int(balance) < 0:
                view.improper_balance()
                continue
            
            account = Account(username = username, balance = balance)
            hashed_pw = Account.set_password(account, password)
            account.save()
            logged_in_homepage(account)
            return 
        if selection == "2":
            username, password = view.get_username(), view.get_password()
            logged_in_account = Account.login(username=username, password=password)
            
            if logged_in_account:
                logged_in_homepage(logged_in_account)
                return
            else:
                print("Invalid credentials supplied")
                continue
        if selection == "3":
            view.goodbye()
            return


def logged_in_homepage(account):
    view.logged_in_screen(account.username, account.balance)
    pass


"""TODO 
   develop the view for the login screen and the controller options for it
   see the below for inspiration
""" 



"""
Sample execution

Welcome to Terminal Trader!
    
    1. create account
    2. login
    3. quit

Your choice: 2.


Main Menu:

    1. see balance & positions
    2. deposit money
    3. look up stock price
    4. buy stock
    5. sell stock
    6. trade history

etc.


you should have useful output if a user inputs a stock that does not exist

you should not allow a user to spend money they don't have or sell
shares they don't have

your display of positions or trades should be well-formatted, don't
just print a python list
"""
