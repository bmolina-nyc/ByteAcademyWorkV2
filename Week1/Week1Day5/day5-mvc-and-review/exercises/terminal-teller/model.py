import json
import os
import view 

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}

def load():
    global data
    with open(DATAPATH, "r") as file_object:
        data = json.load(file_object)

def create_account(customer):
    
    data[]

def login():
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

