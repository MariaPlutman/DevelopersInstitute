from math import pi
# Exercise 1
'''class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_perimeter(self):
        return self.radius * pi * 2

    def get_area(self):
        return self.radius * self.radius * pi

    def __str__(self):
        return 'This is a circle with radius of {:.2f}'.format(self.radius)


if __name__ == '__main__':
    c1 = Circle(2.1)
    print(c1.get_perimeter())
    print(c1.get_area())
    print(c1.radius)
'''

# Exercise 2: Custom List Class

import random
from functools import partial


'''class MyList:
    def __init__(self, l):
        self.lst = l

    def reverse(self):
        rvrs = self.lst.copy()
        rvrs.reverse()
        return rvrs

    def sorted_self(self):
        return sorted(self.lst)

    def random_lst(self):
        one_sample = partial(random.sample, range(10), 5)
        sample = [one_sample() for _ in range(3)]
        return sample


l = [9, 6, 7, 2, 0, 5, 8, 9, 6, 7, 5, 0, 6, 7, 3]
my_list = MyList(l)
print(my_list.reverse())
print(my_list.sorted_self())
print(my_list.random_lst())'''

# Exercise 3: In the Quantum Realm


class QuantumParticle:
    def __init__(self):
        self.position = random.randint(1, 100)
        self.momentum = random.random()
        if random.random() >= 0.5:
            self.spin = 0.5
        else:
            self.spin = -0.5
        self.entangle = None

