# Exercise 1
print("Hello world\n" * 4)

# Exercise 2
print((99 ^ 3) * 8)  # 768

# Exercise 3
name = "Maria"
age = 24
shoe_size = 40
info = print("Hi! My name is", name, "and I'm ", age,
             "years old and I have", shoe_size, "shoe size and I'm ok with that")

# Exercise 4
computer_brand = input("Hi! What is the brand of your computer?")
print("I have a {} computer".format(computer_brand))

# Exercise 6
height = input("What is your height? (in inches) ")
height = int(height)
if (height > 35):
    print("You are tall enough to ride a roller coaster")
else:
    print("You can't ride a roller coaster")

# Exercise 7
number = input("Give me the number: ")
number = int(number)
if (number % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")
