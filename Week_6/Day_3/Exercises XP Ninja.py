import re
# Exercise 1
'''l1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
l2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
l3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
l4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# print list in a single line
print(*l1)

# sort list in descending order
l1.sort(reverse=True)
print(l1)

# print sum of all numbers
print("Sum of all numbers in the list: ", sum(l1))

# print the first and the last number
print("The first and the last number in the list: ", l1[::len(l1)-1])

# print a list of all the numbers greater than 50
list1 = []
for i in l1:
    if i > 50:
        list1.append(i)
print("A list of all the numbers greater than 50: ", list1)

# print a list of all the numbers smaller than 10
list2 = []
for i in l1:
    if i < 10:
        list2.append(i)
print("A list of all the numbers smaller than 10: ", list2)

# print a list of all of the numbers squared
list3 = []
for i in l2:
    list3.append(i**2)
print(list3)

# print the numbers without any duplicates
list4 = list(dict.fromkeys(l2))
print(list4, "The number of numbers without dublicates is: ", len(list4))

# The average of all the numbers
print(sum(l2)/len(l2))

# The largest number
print(max(l2))

# The smallest number
print(min(l2))'''


# Exercise 2
my_para = "There’s still a lot we don’t know about Covid-19, as the news headlines demonstrate on a daily basis. That’s to be expected with a virus that has so quickly and completely consumed the globe, dramatically outpacing testing and mitigation efforts. However, the continued unknowns about this virus shouldn’t obfuscate what we do know to be true about this deadly disease. As the weeks wear on, our failure to act on known medical truths is becoming increasingly unforgivable."
char_num = len(my_para)
print("The text contains {}".format(char_num), "characters")

sentences = my_para.count('.') + my_para.count('!') + my_para.count('?')
print("The text contains {}".format(sentences), "sentencess")

l = my_para.split()
words = len(l)
print("The text contains {}".format(words), "words")

