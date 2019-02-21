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
        cust_account = str(cust_account)
        cust_name = f"{customer[0]} {customer[1]}"
        pin = f"{customer[2]}"
        data[cust_account] = {
                "Name": cust_name,
                "account_number": cust_account,
                "PIN": pin,
                "Balance": 0
        }  
        with open(DATAPATH, "w") as file_object:
               json.dump(data, file_object, indent=2)
        
        return data[cust_account]

def login_user(name, pin):
   for key in (data): #scrolls through account numbers
        if name == data[key]['Name'] and str(data[key]["PIN"]) == pin:
                return data[key] # full user object
   return False

def check_balance(customer):
        balance = customer["Balance"]
        print()
        print(f"Your balance is {balance}")

def withdraw_funds(customer, funds_requested):
        new_balance = int(customer['Balance']) - int(funds_requested)
        user_account_number = customer['account_number']
        data[str(user_account_number)]["Balance"] = new_balance
        with open(DATAPATH, "w") as jsonFile:
                json.dump(data, jsonFile, indent=2)           
        print(f"Your new balance is {new_balance}") 

def deposit_funds(customer, funds_to_deposit):
        new_balance = int(customer["Balance"]) + int(funds_to_deposit)
        user_account_number = customer['account_number']
        data[str(user_account_number)]["Balance"] = new_balance
        with open(DATAPATH, "w") as jsonFile:
            json.dump(data, jsonFile, indent=2) 
        print(f"Your new balance is {new_balance}") 

