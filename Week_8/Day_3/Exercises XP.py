# Exercise 1
class Family:
    def __init__(self):
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]
        self.lastname = "Johns"

    def born(self, **kwargs):
        self.members.append({"name": kwargs["name"],
                             "age": kwargs["age"],
                             "gender": kwargs["gender"],
                             "is_child": kwargs["is_child"]})
        print('Warmest congratulations on the birth of your sweet baby!')

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name and member['age'] >= 18:
                return True

    def __repr__(self):
        print('''The normal family:
    ______________________________________ /n''')
        for member in self.members:
            print(member["name"], member['age'],
                  member["gender"], member["is_child"])


# Exercise 2
class TheIncredibles(Family):
    def __init__(self):
        super().__init__()
        self.members[0]["power"] = "healing ability"
        self.members[1]["power"] = "prophetic visions"
        self.members[0]["incredible_name"] = "Captain America"
        self.members[1]["incredible_name"] = "Moon Knight"

    def born_incredible(self, **kwargs):
        self.born(**kwargs)
        for i, member in enumerate(self.members):
            if member["name"] == kwargs["name"]:
                self.members[i]["power"] = kwargs["power"]
                self.members[i]["incredible_name"] = kwargs["incredible_name"]

    def use_power(self, member):
        for member in self.members:
            if member["name"] == member:
                if member["age"] >= 18:
                    print(member["power"])
                else:
                    raise Exception("Sorry, you haven't power")

    def incredible_presentation(self):
        print('''The super power family:
    ______________________________________
    
    ''')
        for member in self.members:
            print(member["name"], member['age'], member["gender"], member["is_child"], member["power"],
                  member["incredible_name"])


def main():
    my_fam = Family()
    my_fam.__repr__()
    print(my_fam.is_18('Sarah'))
    print(my_fam.born(name='Bella',
                      age=2,
                      gender='Female',
                      is_child=True))

    my_fam.__repr__()

    incredibles = TheIncredibles()

    incredibles.born_incredible(name="Jessica", age=17, is_child=True, gender="female", power="immunity to mind control",
                                incredible_name="Jessica Jones")
    incredibles.born_incredible(name="Bruce", age=10, is_child=True, gender="male", power="regeneration",
                                incredible_name="Hulk")
    incredibles.born_incredible(name="Jack", age=1, is_child=True, gender="male", power="unkown",
                                incredible_name="Silver Surfer")
    incredibles.__repr__()

    incredibles.incredible_presentation()


if __name__ == "__main__":
    main()
