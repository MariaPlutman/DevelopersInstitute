#!/usr/local/bin/python3
import ascii_art

print("Hello, welcome in the ascii art generator !")

user_str = input("What would you like to print today: ")

art = ascii_art.ascii_art(user_str)

print(art)
