# Get a string from the user. The user must provide a string that is 10 characters long.
input_str = input("Please provide some info: ")
if len(input_str) > 10:
    print("Error! Only 10 characters allowed!")
# inform the user what the first and last characters of the string are
else:
    print("The first character of the string is",
          input_str[0], "and the last character of the string is", input_str[-1])

# ‘Build’ the string up: print the first character, then the first 2, then the first 3, etc., until you print the entire string.
word = ''
for i in range(len(input_str)):
    word += input_str[i]
    print(word)

# Swap some of the characters around, then print out this jumbled-up string to the user. Be sure to label it appropriately.


def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


swap("hello", 1, 3)
