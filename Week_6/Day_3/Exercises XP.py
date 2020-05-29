# Exercise
"""basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove the Banana from the list
basket.remove(basket[0])
# Remove “Blueberries” from the list.
basket.remove("Blueberries")
# Put “Kiwi” at the end of the list.
basket.append("Kiwi")
# Add “Apples” at the beginning of the list
basket.insert(0, "Apples")
# Count how many apples in the basket
print(basket.count("Apples"))
# empty the basket
basket.clear()

print(basket)"""

# Exercise 1
'''my_fav_numbers = {4, 7, 22, 14}
my_fav_numbers.update([5, 6])
my_fav_numbers.remove(max(my_fav_numbers))
friend_fav_numbers = {10, 88, 45}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(my_fav_numbers, our_fav_numbers)'''

# Exercise 2
'''my_tuple = ("Banana", "Apples", "Oranges", "Blueberries")
# 2-3
y = list(my_tuple)
y[-1] = "Kiwi"
my_tuple = tuple(y)
# 1,4
a = list(my_tuple)
a[0] = "Apples"
my_tuple = tuple(a)
# 5
num = my_tuple.count("Apples")
print(num)
# 6
# del x
# 7
print(my_tuple)'''

# Exercise 4
'''active = True
while active:
    name = input("What's your name?")
    if name == 'quit':
        active = False
    else:
        toppings = input("Please enter pizza toppings that you want: ")
        print(f"Hello {name}! You choose pizza with: ", toppings)
print("Thank you that choosing us!")'''

# Exercise 6
'''my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.reverse()

for x in my_list:
    print(x) '''

# Exercise 7
"""active = True
my_list = []

while active:
    age = input("What's your age? ")
    age = int(age)
    if age == 'end':
        active = False
    elif age <= 3:
        print("Your ticket is free")
        my_list.append(0)
    elif 12 >= age > 3:
        print("Your ticket is 10$")
        my_list.append(10)
    elif age > 12:
        print("Your ticket is 15$")
        my_list.append(15)

cost = sum(my_list)
print("You need to pay",cost,"$.")"""

# Exercise 8
"""list1 = [10, 21, 4, 45, 66, 93]

for num in list1:
    if num % 2 == 0:
       print(num, end=" ") """

# Exercise 9
"""my_list = []
name = input("Hello! What's your name? ")
age = int(input("What's your age? "))
if 16 <= age <= 21:
    print(name,", enjoy your movie!")
    my_list.append(str(name))
else:
    print(name,", this movie not for you =(")
print (','.join(my_list))"""

# Exercise 10
"""my_list = ['Oliver', 'Jake', 'Connor', 'Harry', 'Jacob', 'Oscar', 'Damian']
name = input("What's your name? ")
age = int(input("Whats your age? "))
if name in my_list and age > 16:
    print(my_list)
elif name in my_list and age < 16:
    my_list.remove(name)
    print(my_list)
else:
    print("You're not in the list")"""
