from menu import Menu
from drink import Drink
from food import Food
import pickle


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

    pickle.dump(m1, open("menu-dump.pkl", "wb"))

