import json

sample_data = {
        "key1" : 5,
        "key2" : 10,
        "key3" : {
                "sub1": 5,
                "sub2": [1,2,3,4,5,6]
            },
        "key4" : None
        }

with open('mydata.json', 'w') as file_object:
    json.dump(sample_data, file_object, indent=2)

# nested keys review
print(sample_data['key3']['sub2'][4])
