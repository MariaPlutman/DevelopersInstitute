import random

# Exercise 1
'''def get_random_temp():
    season = input("What time of year is it? ")
    if season == "winter":
        return random.randrange(-10, 10)
    elif season == "summer":
        return random.randrange(24, 40)
    elif season == "spring":
        return random.randrange(16, 23)
    elif season == "autumn":
        return random.randrange(10, 23)


def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 < temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 < temp < 23:
        print("Nice weather to make a trip")
    elif 24 < temp < 32:
        print("Bring your swimwear, it's time for the beach!")
    elif 32 < temp < 40:
        print("Stay at home with your conditioner!")


main()'''

# Exercise 2


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    val = throw_dice()


throw_until_doubles()