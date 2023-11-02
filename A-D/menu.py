from drink import Drink
from food import Food
from log import *


class Menu:
    def __init__(self, name, address, drinks, foods):
        self.name = name
        self.address = address
        self.drinks = drinks
        self.foods = foods
        log("CRE", f"Создан объект {self.name}")

    def __str__(self):
        log("PRI", f"Взаимодействие с информацией объекта {self.name}")
        menu_str = f"Menu of {self.name} at {self.address}: \n"
        menu_str += "Drinks:\n"
        for i, drink in enumerate(self.drinks):
            menu_str += f"{i + 1}: {str(drink)}\n"
        menu_str += "Foods:\n"
        for i, food in enumerate(self.foods):
            menu_str += f"{i + 1 + len(self.drinks)}: {str(food)}\n"
        return menu_str

    def __len__(self):
        log("PRI", f"Взаимодействие с информацией объекта {self.name}")
        return len(self.drinks) + len(self.foods)

    def __getitem__(self, index):
        log("PRI", f"Взаимодействие с информацией объекта {self.name}")
        try:
            if index < len(self.drinks):
                return self.drinks[index]
            else:
                return self.foods[index - len(self.drinks)]
        except IndexError:
            print("Incorrect index!")

    def __setitem__(self, index, value):
        try:
            if index < len(self.drinks):
                self.drinks[index] = value
            else:
                self.foods[index - len(self.drinks)] = value
            log("INF", f"Изменен объект {self.name}")
        except IndexError:
            print("Incorrect index!")
            log("ERR", f"Ошибка при изменении объекта {self.name}")

    def __delitem__(self, index):
        try:
            if index < len(self.drinks):
                del self.drinks[index]
            else:
                del self.foods[index - len(self.drinks)]
            log("INF", f"Изменен объект {self.name}")
        except IndexError:
            print("Incorrect index!")
            log("ERR", f"Ошибка при изменении объекта {self.name}")

    def __add__(self, other):
        log("INF", f"Изменен объект {self.name}")
        drinks = self.drinks + other.drinks
        foods = self.foods + other.foods
        return Menu("Combined Menu", "Combined Address", drinks, foods)

    def __sub__(self, other):
        log("INF", f"Изменен объект {self.name}")
        drinks = [drink for drink in self.drinks if drink not in other.drinks]
        foods = [food for food in self.foods if food not in other.foods]
        return Menu("Subtracted Menu", "Subtracted Address", drinks, foods)

    def create_txt_file(self, file_name):
        log("PRI", f"Взаимодействие с информацией объекта {self.name}")
        with open(file_name, "w") as f:
            f.write(str(self))
            f.write("\nIngredients for Drinks:\n")
            for drink in self.drinks:
                f.write(f"{drink.name}: {', '.join(drink.comp)}\n")
            f.write("\nIngredients for Foods:\n")
            for food in self.foods:
                f.write(f"{food.name}: {', '.join(food.comp)}\n")


if __name__ == "__main__":
    drinks = [
        Drink("Water", 10, 100, "Non-alcoholic", {"water": 100}),
        Drink("Tea", 100, 350, "Non-alcoholic", {"water": 350, "sugar": 40, "lemon": 10}),
        Drink("Espresso", 100, 50, "Non-alcoholic", {"water": 30, "sugar": 10, "milk": 20})
    ]
    foods = [
        Food("Toast with strawberry jam", 150, 40, 4, ["bread", "strawberry jam", "butter"]),
        Food("Omelette", 300, 150, 10, ["eggs", "milk", "tomatoes", "salt", "paper"]),
        Food("Bearger", 400, 150, 15, ["bun", "bear meat", "tomatoes", "mustard"])
    ]
    m1 = Menu("Cafe", "Arbatskaya street, 8", drinks, foods)

    print(m1, len(m1), m1[2])
    print()
    m1[2] = Drink("Lemonade", 150, 100, "Non-alcoholic", {"water": 100, "sugar": 20, "lemon acid": 15})

    print(m1[2])
    del m1[4]
    print(m1)

    m2 = Menu("Stall", "Arbatskaya street, 8/1",
              [Drink("Cola", 100, 100, "Non-alcoholic", {"Cola": 100})],
              [Food("Hot Dog", 150, 100, 3, ["bun", "sausage", "mustard"])])

    print(m1 + m2)
    m3 = m1 + m2
    m3.create_txt_file("Menu.txt")
