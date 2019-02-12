import model
import view 


def run():
    model.load()
    homepage()


def get_user_info():
    fname = view.get_first_name()   
    lname = view.get_last_name()
    pin = view.get_pin()
    confirmed_pin = view.confirm_pin()
    return [fname, lname, pin, confirmed_pin]


def homepage():
    while True:
        view.show_homepage()
        selection = view.get_input()

        if selection != '1' and selection != '2' and selection != '3':
            view.bad_selection()
        elif selection == '1':
            customer = get_user_info()
            if customer[2] != customer[3]:
                view.no_pin_match()
            else:
                model.create_account(customer)
                customer = model.login_user(f"{customer[0]} {customer[1]}", f"{customer[3]}")
                logged_in_homepage(customer)
                return
        elif selection == '2':
            name = view.login_name()
            pin = view.login_pin()
            if model.login_user(name,pin):
                customer = model.login_user(name, pin)
                logged_in_homepage(customer)
                return
            else:
                view.invalid_login()
                pass
        elif selection == '3':
            view.goodbye()
            return 


def logged_in_homepage(customer):
    while True:
        view.logged_in_homepage(customer)
        selection = view.get_input()
        
        if selection != '1' and selection != '2' and selection != '3' and selection != '4':
            view.bad_selection()
        elif selection == '1':
            balance = model.check_balance(customer)
            print(f'Your balance is {balance}')
        elif selection == '2': 
                funds_requested = view.withdraw_funds()  
                if funds_requested.isdigit() and int(customer["Balance"]) > int(funds_requested):
                    new_balance = model.withdraw_funds(customer, funds_requested)
                    print(f"Your new balance is {new_balance}")
                else:
                    print("You have insufficient funds. Please try again")
        elif selection == '3':
            funds_to_deposit = view.deposit_funds()
            if funds_to_deposit.isdigit():
                new_balance = model.deposit_funds(customer, funds_to_deposit)
                print(f"Your new balance is {new_balance}")
            else:
                print("Please enter a whole number amount")
        elif selection == '4':
            view.goodbye()
            homepage()
            return 

    

if __name__ == "__main__":
    run()
