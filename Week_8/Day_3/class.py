'''my_dict = {}
my_dict['dog'] = 'Rex'
my_dict['dog'] = 'Snowball'
print(my_dict)
'''


'''class OrderedDict(dict):
    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)


o = OrderedDict()
o['dog'] = 'Rex'
print(o)
'''


'''class OrderedDict():
    def __init__(self):
        self.container = {}

    def add(self, key, value):
        if key not in self.container:
            self.container[key] = []

        self.container[key].append(value)

    def get(self, key):
        if key not in self.container:
            return[]
        return self.container[key]

    def __repr__(self):
        msg = ""
        for key, value in self.container:
            msg += "{}-->{} | ".format(key.value)

        return "<OrderedDict {}>".format(msg)


my_dict = OrderedDict()
my_dict.add('dog', 'Rex')
my_dict.add('dog', 'Snowball')'''


'''class Animal:
    def eat(self):
        print("I'm eating")

    def sleep(self):
        print("I'm sleeping")

    def breath(self):
        print("I'm breathing")


class Dog(Animal):
    def run(self):
        print("I'm running")


class Bird(Animal):
    def fly(self):
        print("I'm flying")


class Fish(Animal):
    def sweem(self):
        print("I'm sweeming")

    def breath(self):
        print("I'm breathing under water")


class Platypus(Bird, Fish, Dog):
    pass


my_dog = Dog()
my_bird = Bird()
my_fish = Fish()

my_dog.breath()
my_bird.breath()
my_fish.breath()

print('===')
plati = Platypus()
plati.breath'''


class BookOfSpells():
    def __init__(self):
        self.spells = []

    def add(self, spell):
        self.spells.append(spell)
        print("Added: {}".format(spell.get_description()))


class Spell():
    def __init__(self, name, incantion_duration, incantion_phrase):
        self.name = name
        self.incantion_duration = incantion_duration
        self.incantion_phrase = incantion_phrase

    def get_description(self):
        return "{} --> {}".format(self.name, self.incantion_phrase)

    def execute(self):
        print(self.incantion_phrase.upper())


class DangerousSpell(Spell):
    def execute(self):
        validate = input("Are you want to execute {}? Y/N".format(self.name))
        if validate == 'Y':
            print(self.incantion_phrase.upper())


book = BookOfSpells()

fire_spell = Spell("FireSpell", 2, "May the fire be with me")
ice_spell = Spell("IceSpell", 3, "May the ice be with me")

corona_spell = DangerousSpell("Corona", 3000, "Hey there")

book.add(fire_spell)
book.add(ice_spell)
