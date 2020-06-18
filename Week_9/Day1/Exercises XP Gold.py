# Exercise 1: Object Oriented Star Wars
import random
from abc import ABC, abstractmethod
from statistics import harmonic_mean


class ForceWielder:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(1, 15)
        self.wisdom = random.randint(1, 15)

    def train(self):
        pass

    def fight_method(self, other):
        pass
