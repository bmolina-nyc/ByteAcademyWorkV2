import json
from pprint import pprint


success = False
while not success:
    filename = input("What file to open? ")
    try:
        with open(filename, 'r') as file_object:
            data = json.load(file_object)
            success = True
    except FileNotFoundError:
        print("bad filename")

pprint(data)
