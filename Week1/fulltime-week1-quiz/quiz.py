"""
* Return a list of dictionaries from this data, with each
line of the file corresponding to an element in the dictionary.
"""

def readcurrency(filename):
    printed_text = []
    with open(filename) as file_object:
        text = file_object.readlines()
    for line in text:
        dict_item = {}
        line = line.split()
        dict_item["symbol"] = line[0]
        dict_item["rate"] = line[1]
        printed_text.append(dict_item)
    return printed_text


"""
* Write a second function ```save(filename, data)```
* This takes a filename and the list constructed by the first list.
* It wraps the list in a dictionary with a single key, "data"
* It saves that dictionary to the json file specified by filename 
"""
data_output = readcurrency("currency.txt")

def save(filename, data):
    datalist = []
    datajson = {}
    for line in data:
        datalist.append(line)
        datajson["data"] = datalist  

    final_output = open(filename, "w")
    final_output.write(str(datajson))
    


save("my_output_file.txt", data_output)