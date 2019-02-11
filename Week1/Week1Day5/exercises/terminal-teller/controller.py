import model
import view 


def run():
    model.load()
    homepage()


def homepage():
    while True:
        view.show_homepage()
        selection = view.homepage_input()
        if selection != '1' and selection != '2' and selection != '3':
            print("\nTry again!")
        elif selection == '1':
            customer = view.create_account()
            if customer[2] != customer[3]:
                print("\nPins do not match, please try again\n")
            else:
                model.create_account(customer)
                print(f"Welcome {customer[0]} {customer[1]}")
                logged_in()
                return
        elif selection == '2':
            pass
        elif selection == '3':
            print("Goodbye!")
            return 
    


def logged_in():
    while True
        view.logged_in_main_menu()
        selection = 

if __name__ == "__main__":
    run()
