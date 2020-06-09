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

# Exercise 2


class MyCollection(list):
    def __init__(self, *args, **kwargs):
        super(MyCollection, self).__init__(args[0])
