# Exercise 2
def ex2(a, b):
    if (a > b):
        print("Hello World")
    else:
        print("Bye")


# Exercise 3
while True:
    month = input('''Input the month (from 1 to 12): 
    (enter 'stop' to when you are finished)''')
    month = int(month)
    if 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    elif 9 <= month <= 11:
        print("Autumn")
    elif month == 1 or month == 2 or month == 12:
        print("Winter")
