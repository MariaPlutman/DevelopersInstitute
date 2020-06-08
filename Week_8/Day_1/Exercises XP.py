# Exercise 1
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return self.name, self.age

    def oldest_cat(self):
        results = []
        for cat in cats:
            (self.name, self.age) = cat.get_details()
            results.append((name, age))
        print(f'The oldest cat is {max(results)} years old')


cats = [Cat("zimka", 5),
        Cat("oczko", 10),
        Cat("kotek", 1),
        Cat("edward", 4)]
