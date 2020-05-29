import random
# Exercise 3
'''
a = input("Input the 1st number:")
b = input("Input the 2st number:")
c = input("Input the 3st number:")

if a > b and a > c:
    print(f"The greatest number is:", a)
elif b > a and b > c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)'''

# Exercise 4
'''while True:

    alphabet = input("Input a letter of the alphabet:/n
    (if you want to exit print 'stop')")
    if alphabet == 'stop':
        print('Good bye!')
        break
    elif alphabet in ('a', 'e', 'i', 'o', 'u'):
        print("%s is a vowel." % alphabet)
    else:
        print("%s is a consonant." % alphabet)'''

# Exercise 5
'''target_num, guess_num = random.randint(1, 9), 0
while target_num != guess_num:
    guess_num = int(
        input('Guess a number between 1 and 9 until you get it right : '))
print('Well guessed!')'''

# Exercise 6
'''for number in range(1, 21):
    print(number)'''

# Exercise 7
'''numbers = list(range(1, 1000001))
print(numbers)'''

# Exercise 8
'''numbers = list(range(1, 1000001))
# print(numbers)
print('Min number in list is:', min(numbers), 'and max number is:',
      max(numbers), "sum of the numbers in list is:", sum(numbers))'''

# Exercise 9
'''listOfElems = ['Hello', 'Ok', 'is', 'Ok',
               'test', 'this', 'is', 'a', 'test', 'Ok']
indexPos = listOfElems.index('Ok')
print('First index of element "Ok" in the list : ', indexPos)'''

# Exercise 10
'''l1 = [1, 2, 3]
l2 = [4, 5, 6]
joined_list = [*l1, *l2]
print(joined_list)'''
