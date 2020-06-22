from ex_xp_module import ex1
from random import randint
import random
import string

# Exercise 1
print(ex1("Maria"))

# Exercise 2
'''def ex2():
    answer = randint(1, 100)
    while True:
        try:
            guess = int(input('Guess a number 1~100: '))
            if 0 < guess < 101:
                if guess == answer:
                    print('Great choice!')
                    break
                else:
                    print('Try another number')
        except ValueError:
            print('Please enter a number 1~100: ')
            continue
ex2()'''

# Exercise 3
'''def randomString(stringLength=5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


print("Random String is", randomString())
'''
