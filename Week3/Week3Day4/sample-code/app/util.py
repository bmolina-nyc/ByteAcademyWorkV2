# from hashlib import sha512
# import requests

FAKE_PRICES = {
        'stok': 3.50
    }

def hash_password(password):
    """ WEEK 4 TODO: encrypt with sha512 & a salt """
    return password

def get_price(ticker):
    if ticker in FAKE_PRICES.keys():
        return FAKE_PRICES[ticker]

    """ WEEK 4 TODO: get price from IEXTrading API """
    return ord(ticker[0]) * 5.731
