from datetime import *
# Exercise 1


def get_age(year, month, day):
    today = date.today()
    dob = date(year, month, day)
    numberOfDays = (today - dob).days
    age = numberOfDays // 365
    return age


# Exercise 2
def make_shirt(size='large', text='I love Python!'):
    print(f'You ordered shirt in {size} size with text "{text}"')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')

# Exercise 3


def describe_city(city, country):
    print(f'{city.title()} is in {country.title()}')


describe_city("odessa", "ukraine")

# Exercise 4


def display_message():
    print("Hey! In this chapter I am learning the functions")


display_message()
