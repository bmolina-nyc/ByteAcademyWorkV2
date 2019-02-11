import json
import os
import view 

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}

def create_account(customer):
    with open(DATAPATH, "w") as file_object:
        data = json.load(file_object)
        print(data)

def login():
    pass

def load():
    pass

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

