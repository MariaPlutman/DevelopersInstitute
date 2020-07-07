# Exercise 1
# Use python to create a random secret key composed of 256 random letters.
import os

key = os.urandom(256)
print(key)
