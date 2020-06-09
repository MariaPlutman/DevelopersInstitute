# Exercise 1: Restaurant Menu Manager
'''class MenuManager:
    def __init__(self):
        self.menu = {
            "Soup": [10, "B", False],
            "Hamburger": [15, "A", True],
            "Salad": [18, "A", False],
            "French Fries": [5, "c", False],
            "Beef Bourgignon ": [25, "B", True],
        }

    def add_item(self, name, price, spice, gluten):
        self.menu[name] = [price, spice, gluten]

    def update_item(self, name, price, spice, gluten):
        if name in self.menu:
            self.menu[name] = [price, spice, gluten]
        else:
            print(f"{name} is not in the menu")

    def remove_item(self, name):
        if name in self.menu:
            del self.menu[name]
            print(self.menu)
        else:
            print(f"{name}is not in the menu")


menu = MenuManager()

menu.add_item("Pasta", 16, "A", True)
menu.add_item("Sandwich", 7, "B", True)
menu.update_item("Salad", 21, "A", False)
menu.update_item("Salad with crackers", 21, "A", False)
menu.remove_item("Sushi")
menu.remove_item("Soup") '''

# Exercice 2: Old MacDonald’s Farm
