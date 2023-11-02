from log import *


class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        log("CRE", f"Создан объект {self.name}")


if __name__ == "__main__":
    tow = Item('Paper towel', 10)
    print(tow.name, tow.price, "Rub")
