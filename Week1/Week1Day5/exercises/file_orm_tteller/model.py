from random import randint()
import json

class NegativeDepositException(Exception):
    pass

class TellerAccount:

    datastore = "data.json"

    def __init__(self):
        self.acct_number = ""
        self.name = ""
        self.balance = 0.0
        self.pin = ""

    def save(self):
        try:
            with open(self.datastore, 'r') as file_object:
                data = json.load(file_object)
        except FileNotFoundError:
            data = {}

        if self.acct_number:
            data[self.acct_number] = {
                        "name": self.name,
                        "balance": self.balance,
                        "pin": self.pin
                    }
        
            with open(self.datastore, 'w') as file_object:
                json.dump(data, file_object, indent=2)

    @classmethod
    def login(cls, acct_number, pin):
        try:
            with open(cls.datastore, "r") as file_object:
                data = json.load(file_object)
        except FileNotFoundError:
            return None
        if acct_number in data and data[acct_number]["pin"] == pin:
            account_dic = data[acct_number]
            account = cls()
            account.acct_number = acct_number
            account.pin = pin
            account.name = account_dic["name"]
            account.balance = account_dic["balance"]
            return account
        return None
    
    @classmethod
    def new_acct_num(cls):
        with open(cls.datastore, "r") as file_object:
            data = json.load(file_object)
        new_acct_num = None
        while new_acct_num is None or new_acct_num in data:
            new_acct_num = str(randint(10 ** 9, 10 ** 10 - 1))

    def withdraw(self, amount):
        if amount > self.balance or amount < 0.0:
            raise ValueError("Insufficient Funds")
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0.0:
            raise ValueError("Negative deposit")
        self.balance += amount

    """
    def __bool__(self):
        if self.acct_number:
            return True
        return False
    """

class GameBoard:
    def __getitem__(self, index):


g = GameBoard
g[someval]
