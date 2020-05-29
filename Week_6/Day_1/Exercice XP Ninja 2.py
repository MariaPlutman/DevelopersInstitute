# Exercise 2
while True:
    alphabet = input('''Input a letter of the alphabet: 
    (if you want to exit print 'stop')''')
    if alphabet == 'stop':
        print('Good bye!')
        break
    elif alphabet in ('a', 'e', 'i', 'o', 'u'):
        print("%s is a vowel." % alphabet)
    else:
        print("%s is a consonant." % alphabet)

# Exercise 3
import re
p = input("Input your password")
x = True
while x:
    if (len(p) < 6 or len(p) > 12):
        break
    elif not re.search("[a-z]", p):
        break
    elif not re.search("[0-9]", p):
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[$#@]", p):
        break
    elif re.search("\s", p):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Not a Valid Password")

# Exercise 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
characters = 0
characters += sum(len(word) for word in my_text)
print(characters)
