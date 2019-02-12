import model
import view 


def run():
    model.load()
    homepage()

def create_account():
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
            print("\nTry again!")
        elif selection == '1':
            customer = create_account()
            if customer[2] != customer[3]:
                print("\nPins do not match, please try again\n")
            else:
                model.create_account(customer)
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
                print()
                print("Invalid Login - please try again")
                pass
        elif selection == '3':
            print("Goodbye!")
            return 


def logged_in_homepage(customer):
    view.logged_in_homepage(customer)
    selection = view.get_input()

    

if __name__ == "__main__":
    run()
