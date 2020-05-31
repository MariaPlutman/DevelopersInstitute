import re
# Exercise 1
'''fruits = input("What's your favorite fruits? \n(saperate them with a space)")
favorite_fruits = []
current_word = ""
for letter in favorite_fruits:
    if letter == " ":
        fruits.append(current_word)
        current_word = ""
    else:
        current_word += letter.lower()

favorite_fruits.append(current)

if fruits.lower() in favorite_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy it too!')'''


# Exercise 2
'''password = input("Input your password")
x = True
while x:
    if (len(password) < 6 or len(password) > 12):
        break
    elif not re.search("[a-z]", password):
        break
    elif not re.search("[0-9]", password):
        break
    elif not re.search("[A-Z]", password):
        break
    elif not re.search("[$#@]", password):
        break
    elif re.search("\s", password):
        break
    else:
        print("Valid Password")
        x = False
        break
if x:
    print("Not a Valid Password")'''

# Exercise 3
"""my_list = [i for i in range(3, 31) if i % 3 == 0]
print(my_list)"""

# Exercise 4
'''list1 = [1, 2, 3, 4, 5, 6, 7]
list1.insert(4, 10)
print(list1) '''

# Exercise 5
car_manufacturers = "Toyota Honda Chevrolet Ford Mercedes-Benz Jeep"
car_manufacturers = car_manufacturers.split()
print(
    f'In the list we have {len(car_manufacturers)} most popular car manufacturers')
print(car_manufacturers)

# Exercise 6
'''nl = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))
print(','.join(nl))'''

# Exercise 7
"""count = 0
space_count = input()
print("The original string is : " +  space_count)
for i in space_count:
    if(i.isspace()):
        count += 1
print("The number of blank spaces is: ",count)"""

# Exercise 8
"""my_string = input()
print("The original string is : " +  my_string)
res = len(my_string.split())
print ("The number of words in string are : " +  str(res)) """

# Exercise 9
"""def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')"""
