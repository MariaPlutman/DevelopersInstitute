'''def my_func():
    print("Hello world, I am my_func")
    print("I am very happy to be here")


my_func()


def say_hello(username):
    print("Hello "+username)


say_hello("Rick")
say_hello("Morty")

# function that accept more than one argument


def say_hello2(username, language):  # language="EN"
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)


say_hello2("Rick", "EN")'''

# ex 1
'''def make_shirt(size, text):
    print("Creating a {} shirt with <{}>".format(size, text))


make_shirt("Medium", "Peace on the world")
make_shirt(text="Peace on the world", size="Medium")'''

# ex 2
'''def lower_names(names):
    new = []
    for i in range(len(names)):
        names[i] = names[i].lower()
        if names[i][0] not in "aeuoiy":
            new.append(names[i])
    return new


names = ["Rick", "Morty", "SuMmer", "iRick"]
print(lower_names(names)) '''

# ex 3
'''def describe_city(city, country):
    print(f'{city} is in {country}')


describe_city("Odessa", "Ukraine")'''

# ex 4
'''def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax, l.index(max(l))


l = [77, 48, 19, 17, 93, 90]
print(highestNumber(l))'''

# ex 5
'''def frame_string(*words):
    size = max(len(word) for word in words)
    print('*' * (size + 4))
    for word in words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))


frame_string("Hello", "World", "in", "reallylongword", "a", "frame")'''

# ex 6
'''morse_code = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += morse_code[letter] + ' '
        else:
            cipher += ' '
    return cipher


def main():
    message = "DEVELOPERS INSTITUTE"
    result = encrypt(message.upper())
    print(result)


main()'''


def age():
    user_age = input("How old are you?\n>>> ")
    #######
    try:
        user_age = int(user_age)
        print("I AM AFTER USER_AGE")
    except:
        print("Your age is not a real age")
        user_age = 0


age()
print("Next year, you will be {} years old".format(user_age+1))
