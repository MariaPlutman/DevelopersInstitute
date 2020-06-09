# Exercise 1
'''class Cat:
    species = 'mammal'
    _Instances = []
    @classmethod
    def getoldest(cls):
        _Instance = max(cls._Instances, key=lambda Instance: Instance.age)
        return ("Oldest {} is {}: {} years old.".format(cls.__name__, _Instance.name, _Instance.age))

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__._Instances.append(self)


Cat("Tom", 1)
Cat("Bamba", 2)
Cat("Lily", 3)
Cat("Doogl", 4)
print(Cat.getoldest())'''

# Exercise 2
'''class Dog():
    _Instances = []

    @classmethod
    def is_bigger(cls):
        _Instance = max(
            cls._Instances, key=lambda Instance: Instance.height)
        return ("Bigger dog is {}".format(_Instance.name))

    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.__class__._Instances.append(self)

    def talk(self):
        print("Wouaf!")

    def jump(self):
        jumpDog = self.height * 2
        print("The height of the " + str(self.name) + " when he jumps:", jumpDog)


Davids_dog = Dog('Rex', 50)
Sarahs_dog = Dog('Teacup', 20)
Davids_dog.name, Davids_dog.height
Sarahs_dog.name, Sarahs_dog.height
Davids_dog.jump(), Davids_dog.talk()
Sarahs_dog.jump(), Sarahs_dog.talk()

print(Dog.is_bigger())'''

# Exercise 3
'''class Zoo():
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name
        self.pen = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            print(f'Goodbye {animal_sold}!')
            self.animals.remove(animal_sold)

    def sort_animal(self):
        self.animals.sort(key=str.lower)

    def get_pen(self):
        print(self.pen)


ramatGanSafari = Zoo("Safari")
ramatGanSafari.add_animal("Lion")
ramatGanSafari.add_animal("Zebra")
ramatGanSafari.add_animal("Tiger")
ramatGanSafari.add_animal("Camel")
ramatGanSafari.get_animals()
ramatGanSafari.sell_animal("Zebra")
ramatGanSafari.get_animals()
ramatGanSafari.sort_animal()
ramatGanSafari.get_animals()
'''
