# Exercise 1
friends_ages = {
    "Monty": 25,
    "Monika": 29,
    "Danis": 31
}

# Exercise 2
ex2_dict = {
    0: 10,
    1: 20
}

ex2_dict.__setitem__(2, 30)
print(ex2_dict)

# Exercise 3
products = {'SMART WATCH': 550,
            'PHONE': 1000,
            'PLAYSTATION': 500,
            'LAPTOP': 1550,
            'LAPTOP': 1550,
            'MUSIC PLAYER': 600,
            'TABLET': 400,
            'TABLET': 400
            }

for key in products:
    print("{}: {}".format(key, products[key]))

items = iter(products.items())
while True:
    try:
        item = next(items)
        print(*item)
    except StopIteration:
        break

# Exercise 4
# remove duplicates values from Dictionary
result = {}

for key, value in products.items():
    if value not in result.values():
        result[key] = value

print(result)

# Exercise 5
# check if a given key already exists in a dictionary
result = {}

for key in products.items():
    if key not in result.keys():
        result[key] = value

print(result)

# Exercise 6
# concatenate following dictionaries to create a new one
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = dic1
dic4.update(dic2)
dic4.update(dic3)

print(dic4)

# Exercise 7
list1 = ['Rick', 'Donald', 'Mickey', 'Mario']
list2 = ['Sanchez', 'Duck', 'Mouse', 'Kart']

my_dict = dict(zip(list1, list2))
print(my_dict)

# Exercise 8
products2 = {'SMART WATCH': 550,
             'PHONE': 1000,
             'PLAYSTATION': 500,
             'LAPTOP': 1550,
             'MUSIC PLAYER': 600,
             'TABLET': 400
             }


money = int(input('How much money you got? '))
for item in products:
    if money >= products[item]:
        print(f'You can buy: {item}')

# Exercise 9
num = int(input('Give me anumber: '))
