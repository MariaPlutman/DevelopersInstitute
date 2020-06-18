import os
import random
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(THIS_FOLDER, 'wordlist.txt')

# Exercise 1 – Random Sentence Generator


def get_words_from_file():
    with open(filepath) as fp:
        flat_list = [word for line in fp for word in line.split()]
    return flat_list


def get_random_sentence(length):
    l = get_words_from_file()
    sentence = ' '.join(random.choices(l, k=length))
    return sentence.lower()


print(get_random_sentence(5))

