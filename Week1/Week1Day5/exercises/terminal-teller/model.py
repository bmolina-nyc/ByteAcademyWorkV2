import json
import os
import random

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}

def load():
    global data
    with open(DATAPATH, "r") as file_object:
        data = json.load(file_object)


def create_account(customer):
        cust_account = random.randint(10000,99999)
        cust_name = f"{customer[0]} {customer[1]}"
        data[cust_name] = {
                "Name": f"{customer[0]} {customer[1]}",
                "account_number": cust_account,
                "PIN": f"{customer[2]}",
                "Balance": 0
        }  
        with open(DATAPATH, "w") as file_object:
               json.dump(data, file_object, indent=2)
        print(data)

def login_user(name, pin):
   if name in data and data[name]["PIN"] == pin:
           return data[name]
   else:
           return False


def quit():
    pass

def get_balance():
    pass


def withdraw_funds():
    pass

def deposit_funds():
    pass

def logout():
    pass

