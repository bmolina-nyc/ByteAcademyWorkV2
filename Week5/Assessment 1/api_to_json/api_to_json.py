import requests 
import os 
import csv
import json
from pprint import pprint

PATH = os.path.dirname(__file__)
DATA = "SYMBOL_chart.json"
DATAPATH = os.path.join(PATH, DATA)

def api_call(ticker):
    try: 
        response = requests.get('https://api.iextrading.com/1.0/stock/{}/chart'.format(ticker))
        payload = response.json()
        return payload
    except ValueError:
        return False

def api_download():
    data = {}
    while True:
        ticker = input("enter a ticker symbol ")
        payload = api_call(ticker)
        if not payload:
            print("please try again ")
            continue
        else:
            with open(DATA, "w+") as json_file:
                columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'unadjustedVolume', 'change', 'changePercent', 'vwap', 'label' , 'changeOverTime']
                writer = csv.DictWriter(json_file, fieldnames=columns)
                data[ticker] = payload
                json.dump(data, json_file)


# api_download()
#goog, aapl, tsla