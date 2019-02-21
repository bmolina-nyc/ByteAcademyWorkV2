import sqlite3
import random
import os
import schema
from pprint import pprint

PATH = os.path.dirname(__file__)
DBFILENAME = 'backend_data.db'
DBPATH = os.path.join(PATH, DBFILENAME)


def GET_LAST_ACCOUNT():
        connection = sqlite3.connect('backend_data.db')
        cursor = connection.cursor()
        SQL = "SELECT account_holder, account_number,pin, balance,pk FROM accounts ORDER BY pk DESC limit 1;"
        cursor.execute(SQL)
        return cursor.fetchall() #[(account_holder,account_number, pin, balance)]


def create_account(customer):
        cust_account = random.randint(10000,99999)
        cust_account = str(cust_account)
        cust_name = f"{customer[0]} {customer[1]}"
        pin = f"{customer[2]}"

        with sqlite3.connect(DBPATH) as connection:
                curs = connection.cursor()
                SQL = "INSERT INTO accounts(account_holder, account_number, pin, balance) VALUES(?, ?, ?, ?);"
                curs.execute(SQL, (cust_name, cust_account, pin, 0))
        return GET_LAST_ACCOUNT()

        
def login_user(name, pin):
        with sqlite3.connect(DBPATH) as connection:
                curs = connection.cursor()
                SQL = "SELECT account_holder, account_number, pin, balance, pk FROM accounts WHERE account_holder= ? AND pin= ?;"
                curs.execute(SQL, (name, pin))
                return curs.fetchall()

def update_funds(customer, funds, action):
        current_customer_money = customer[0][3]
        current_customer_money = int(current_customer_money)
        funds = int(funds)

        if action == "W":
                current_customer_money -= funds
        elif action == "D":
                current_customer_money += funds
      
        connection = sqlite3.connect('backend_data.db')
        SQL = "UPDATE accounts SET balance = ? WHERE account_number = ?;"
        curs = connection.cursor()
        curs.execute(SQL,(current_customer_money, customer[0][1]))            
        connection.commit()

        return curs.fetchall()
    
def get_customer(primary_key):
        connection = sqlite3.connect('backend_data.db')
        curs = connection.cursor()
        SQL = "SELECT account_holder, account_number, pin, balance FROM accounts WHERE pk=?;"
        curs.execute(SQL,(primary_key,)) 
        return curs.fetchall()