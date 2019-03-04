import os
import json
from pprint import pprint 
import csv

PATH = os.path.dirname(__file__)
DATA = "aapl.json"
DATAPATH = os.path.join(PATH, DATA)

jsondata = {} 
def openfile(TXT="tothelighthouse.txt"):
    with open(TXT, 'r') as file:
        lines = file.readlines()
        line_count = 0
        for line in lines:
            line_count += 1
        print(line_count)
        return lines

# print(openfile())

def newfile(file="linecount.txt"):
    with open(file, "w") as file:
        for line in openfile():
            file.write(str(len(line)))
            file.write("\n")


# print(newfile())


with open(DATA) as file:
    file_lines = file.readlines()
    new_dic = {}
    # new_dic['companyName'] = data['companyName']
    # new_dic['latestPrice'] = data['latestPrice']
    # new_dic['marketCap'] = data['marketCap']

    with open('AAPLprice.json', "w") as csv_file:
        columns = ["companyName", "latestPrice", "marketCap"]
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        for row in file_lines:
            writer.writerow(row)
                # writer.write
    #     writer.writeheader()
    #     for data in writer:
    #         writer.writerow(data)

     

    #     json.dump(data, new_dic)

    #     with open('dict.csv', 'w') as csv_file:
    # writer = csv.writer(csv_file)
    # for key, value in mydict.items():
    #    writer.writerow([key, value])