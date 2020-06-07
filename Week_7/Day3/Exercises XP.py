# Exercise 1
def favorite_book(title):
    return f'One of my favorite books is {title}'


print(favorite_book("Alice in Wonderland"))

# Exercise 2


def make_shirt(size, text):
    return f'You ordered shirt in {size} size with text "{text}"'


print(make_shirt("medium", "VOGUE"))
print(make_shirt(size="large", text="You are my sunshine"))

# Exercise 3


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['Arik', 'Lola', 'Ariel', 'Beni']


# Exercise 4


def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)


make_great(magicians)
show_magicians(magicians)

# Exercise 5


def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge()
