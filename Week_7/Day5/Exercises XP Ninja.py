# Exercise 1
# Write a function to find the max of a list
'''def find_max(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max
print(find_max([0, 1, 3, 50]))'''

# Exercise 2
# Write a function that return factorial of a number
'''def Factorial():
    num = int(input("Enter a number: "))
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
    print("The factorial of", num, "is", factorial)
Factorial()'''

# Exercise 3
# Write a function to find the sum of an array without using the built in function:
'''def Summ(list):
    sum = 0
    for x in list:
        sum += x
    return sum
my_list = [1, 5, 4, 2]
print(Summ(my_list))'''

# Exercise 4
# Write a function that counts an element in a list(without using the count method):
'''def list_count(lst, x):
    count = 0
    for el in lst:
        if (el == x):
            count += 1
    return count
print(list_count(['a', 'a', 't', 'o'], 'a'))'''

# Exercise 5
# Write a function that returns the L2-norm(square root of the sum of squares) of the sum of a list:
'''def Norm(numbers):
    squared_numbers = [number ** 2 for number in numbers]
    sum = 0
    for x in squared_numbers:
        sum += x
    L2 = sum**(1/2)
    return round(L2)
numbers = [1, 2, 2]
print(Norm(numbers))'''

# Exercise 6
# Write a function to find if an array is monotonic(sorted either ascending of descending)


def isMono(my_list):

    return (all(my_list[i] <= my_list[i + 1] for i in range(len(my_list) - 1)) or
            all(my_list[i] >= my_list[i + 1] for i in range(len(my_list) - 1)))


my_list = [7, 6, 5, 5, 2, 0]
# my_list = [2, 3, 3, 3]
# my_list = [1, 2, 0, 4]

print(isMono(my_list))
