# Exercice 1
'''class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def talk(self):
        print("Wouaf!")

    def jump(self):
        jumpDog = self.height * 2
        print("The height of the " + str(self.name) + " when he jumps:", jumpDog)


Davids_dog = Dog('Snowball', 50)
Sarahs_dog = Dog('Cookie', 20)

Davids_dog.name, Davids_dog.height
Sarahs_dog.name, Sarahs_dog.height
Davids_dog.jump(), Davids_dog.talk()
Sarahs_dog.jump(), Sarahs_dog.talk()'''

# Exercice 2
'''class Car():
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def describe(self):
        print(
            f'This is the {self.color} {self.brand} {self.model} {self.year}')


my_car = Car("BMW", "x6", "black", 2018)
my_car.describe()
'''

# Exercice 3
'''class Car():
    def __init__(self, brand, model, color, fuel_capacity):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel_capacity = fuel_capacity
        self.current_fuel = fuel_capacity

    def describe(self):
        print(
            f'This is the {self.color} {self.brand} {self.model}')

    def travel(self, length):
        consumed_fuel = length * 20

        if consumed_fuel > self.current_fuel:
            print("You don'n have enough fuel to travel this distance")

        self.current_fuel -= consumed_fuel

        print(f'You have {self.current_fuel} liters left')

    def add_fuel(self, quantity):
        self.current_fuel += quantity
        if self.current_fuel > self.fuel_capacity:
            self.current_fuel = self.fuel_capacity

            print(f'Added fuel, you now have {self.current_fuel} liters')


my_car = Car("BMW", "x6", "black", 2018)
my_car.travel(5)
my_car.add_fuel(200) '''

# Exercice 4
'''class Character():
    def __init__(self, name, level, life_points):
        self.name = name
        self.level = level
        self.life_points = life_points

        self.max_life_points = life_points

    def level_up(self):
        self.level += 1
        self.max_life_points += 5
        self.life_points = self.max_life_points
        print(f'{self.name} is leveled up')

    def is_alive(self):
        if self.life_points > 0:
            return True
        return False

    def hit_points(self, hit_points):
        self.life_points -= hit_points
        if self.life_points < 0:
            self.life_points = 0
            print(f'{self.name} is dead')

    def heal(self):
        self.life_points += 30
        if self.life_points > self.max_life_points:
            self.life_points = self.max_life_points
'''

# Exercice 5
'''class Hotel():
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms

        self.residents = 0

    def check_in(self):
        if self.residents == self.rooms:
            print("Sorry the hotel is full!")

    def check_out(self):
        self.residents -= 1'''


class FamilyTree():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.companion = None
        self.children = []

    def marry(self, human):


