'''class Animal:
    def __init__(self):
        self.alive = True

    def die(self):
        self.alive = False


class Farm(Animal):
    def __init__(self, animals_num):
        self.animals = []
        for i in range(animals_num):
            self.animals.append(Animal())

    def new_year(self):
        # 1st way
        alives = 0
        for animal in self.animals:
            if animal.alive:
                alives += 1

        # 2nd way
        alives = len([a for a in self.animals if a.alive])
        will_die = alives // 2'''


'''class Computer:
    objs_nb = 0

    def __init__(self, protected):
        self.protected = protected

        self.id = Computer.objs_nb
        Computer.objs_nb += 1
        self.hacked = False


class Network:
    def __init__(self):
        self.computers = []

    def add_computer(self, protected):
        computer = Computer(protected)
        self.computers.append(computer)

    def propagation(self):
        hacked_pc = [pc for oc in self.computers if pc.hacked]
        healthy_pc = [pc for pc in self.computers if not pc.hacked]

        for pc in hacked_pc:
            cmp1 = healthy_pc.pop()
            cmp1.hack()

            cmp2 = healthy_pc.pop()
            cmp2.hack()

    def all_infected(self):
        for pc in self.computers:
            if not pc.hacked:
                return False
        return True

    @property
    def hacked_computers(self):
        hacked_pc = [pc for self.computers if pc.hached]'''


def run_3times(func):
    def newfunk(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)
    return newfunk


@run_3times
def say_hello():
    print("Hello world!")


def int_or_repeat(f):
    def newf(*args, **kwargs):
        while True:
            result = f(*args, **kwargs)
            if type(result) == int:
                return result
    return newf


@int_or_repeat
def ask_age():
    age = input("What is your age?")
    return age
