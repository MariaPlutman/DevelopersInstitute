import json
from collections import OrderedDict

# Exercise 1
with open("/Users/user/Desktop/DevelopersInstitute/Week_10/Day_3/ex1.json", "r") as file:
    data = json.load(file)
    print(data["company"]["employee"]["payble"]["salary"])

# Exercise 2
with open("/Users/user/Desktop/DevelopersInstitute/Week_10/Day_3/ex2.json", "w") as file:
    sampleJson = {"id": 1, "name": "value2", "age": 29}
    dict_keys = sampleJson.keys()
    dict_keys = sorted(dict_keys)
    new_dict = {}
    for key in dict_keys:
        new_dict[key] = sampleJson[key]
    json.dump(new_dict, file)
