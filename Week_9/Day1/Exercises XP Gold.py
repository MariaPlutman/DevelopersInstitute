# Exercise 1: Object Oriented Star Wars
import random
from abc import ABC, abstractmethod


class ForceWielder:
    def __init__(self, name):
        self.name = name

    def power(self):
        return random.randint(1, 15)

    def wisdom(self):
        return random.randint(1, 15)

    def train(self):
        pass

    def fight_method(self):
        pass
