# Exercise 1
'''keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)
'''

# Exercise 2
store = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': ['France -> blue', 'Spain -> red', 'US -> pink', 'green']
}

more_on_store = {
    'creation_date': 1975,
    'number_stores': 10000
}

store['number_stores'] = 2  # 1
print("The clients of", store['name'], "are people that loves fashion.")  # 2
store['country_creation'] = 'Spain'  # 3
if 'international_competitors' in store.keys():  # 4
    store['international_competitors'].append("Desigual")
store.pop('creation_date')  # 5
print(store['international_competitors'][-1])  # 6
color = store['major_color'][2]
print(f'The major color in the {color}')  # 7
print(len(store))  # 8
print(store.keys())  # 9
store.update(more_on_store)  # 10
print(store['number_stores'])


print(store)
