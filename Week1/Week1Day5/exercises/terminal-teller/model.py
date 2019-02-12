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

def login_user(name, pin):
   if name in data and data[name]["PIN"] == pin:
           return data[name]
   else:
           return False

def check_balance(customer):
        balance = customer["Balance"]
        print(f"Your balance is {balance}")

def withdraw_funds(customer, funds_requested):
        new_balance = int(customer['Balance']) - int(funds_requested)
        cust_name = customer["Name"]
        update = {"Balance": new_balance} 
        data[cust_name].update(update)
        with open(DATAPATH, "w") as jsonFile:
                json.dump(data, jsonFile, indent=2)           
        print(f"Your new balance is {new_balance}") 

def deposit_funds(customer, funds_to_deposit):
    new_balance = int(customer["Balance"]) + int(funds_to_deposit)
    cust_name = customer["Name"]
    update = { "Balance": new_balance }
    data[cust_name].update(update)
    with open(DATAPATH, "w") as jsonFile:
            json.dump(data, jsonFile, indent=2) 
    print(f"Your new balance is {new_balance}") 

