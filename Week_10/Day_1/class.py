import wikipedia
from collections import Counter


def seach_a_word():
    word = input("What you want to seach? ")
    w = wikipedia.page(word)
    text = w.content
    print(f'')


seach_a_word()
