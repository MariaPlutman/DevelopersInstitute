#!/usr/local/bin/python3
import requests


def get_ascii_chars(file):
    content = open(file, 'r').read().replace("\n", "")

    unified_letters = content.split("@@")

    # 1st way: list comprehension
    letters = [l.split("@") for l in unified_letters]

    return letters


def get_ascii_chars_from_internet(url):
    content = requests.get(url).text
    unified_letters = content.split("@@")

    # 1st way: list comprehension
    letters = [l.split("@") for l in unified_letters]

    return letters


def get_char(char, letters):

    char_ix = ord(char) - 33

    letter = letters[char_ix]
    return letter


def create_string(ascii_letters):
    # TODO: Add maxchars
    ascii_string = ""
    for ix in range(5):
        for letter in ascii_letters:
            if letter[0] == '':
                continue
            ascii_string += letter[ix]

        ascii_string += "\n"

    return ascii_string


def ascii_art(text):
    letters = get_ascii_chars(
        "/Users/user/Desktop/DevelopersInstitute/Week_10/Day_1/ascii_art/fonts/avatar.flf")
    ascii_letters = []
    # Loading every ascii converted letter
    for letter in text:
        converted = get_char(letter, letters)
        ascii_letters.append(converted)

    # Create a string out of this list
    ascii_string = create_string(ascii_letters)

    return ascii_string
