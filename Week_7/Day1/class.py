'''age_var = 'age'
my_dog = {
    'name': 'Albert',
    'age': 8.5,
    'good_dog': True
}

# Create a new entry
my_dog['lovely_food'] = "cucumber"

# Modify an existing pair
my_dog[age_var] += 1

# Delete keys in dict
del my_dog['age']

print(my_dog)

# Running a fot loop on a dictionary (give the keys)
for element in my_dog.items():  # my_dog.values(), .keys()
    print(element)
'''


list1 = ['Rick', 'Donald', 'Mickey', 'Mario']
list2 = ['Sanchez', 'Duck', 'Mouse', 'Kart']
print({list1[i]: list2[i] for i in range(len(list1))})
