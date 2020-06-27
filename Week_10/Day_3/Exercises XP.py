import json

# Exercise 1
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
} """

data = json.loads(sampleJson)
print(data["company"]["employee"]["payble"]["salary"])

# Exercise 2
with open("/Users/user/Desktop/DevelopersInstitute/Week_10/Day_3/ex2.json", "w") as file:
    sampleJson2 = """{"id": 1, "name": "value2", "age": 29}"""
    data = json.loads(sampleJson2)
    sorted_json = json.dumps(data, indent=2, sort_keys=True)
    file.write(sorted_json)
