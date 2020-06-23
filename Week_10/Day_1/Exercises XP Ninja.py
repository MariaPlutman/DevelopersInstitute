import random
import string
from faker import Faker
from datetime import *
# Exercise 1
today = date.today()
dob_str = input("What is your Date of Birth? dd/mm/yyyy")
dob_data = dob_str.split("/")
dobDay = int(dob_data[0])
dobMonth = int(dob_data[1])
dobYear = int(dob_data[2])
dob = date(dobYear, dobMonth, dobDay)

numberOfDays = (today - dob).days
age = numberOfDays // 365
numberOfmin = age * 525600
print("You have spent " + str(numberOfmin) + " minutes on Earth.")

# Exercise 2
'''user = {}
fake = Faker(['it_IT', 'en_US', 'ja_JP'])
user['name'] = fake.name()
user['adress'] = fake.address()
print(user)'''


# Exercise 3: Python Password Generator
'''def pwd():
    pwd = ""
    count = 0
    length = int(
        input("Input your password length between 6~30: "))
    while count != length:
        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        everything = upper + lower + num + symbol

        pwd += random.choice(everything)
        count += 1
        continue

    if count == length and length >= 6 and length <= 30:
        print(pwd)
    else:
        print("Length between 6~30, try again")


pwd()'''
