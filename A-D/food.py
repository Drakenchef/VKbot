from item import Item
from log import *


class Food(Item):

    def __init__(self, name, price, weight, cooking_time, comp=None):
        super().__init__(name, price)
        self.weight = weight
        self.cooking_time = cooking_time
        self.comp = comp

    def change_time(self, cooking_time):
        self.cooking_time = cooking_time
        log("INF", f"Изменен объект {self.name}")

    def new_comp(self, comp):
        self.comp = comp
        log("INF", f"Изменен объект {self.name}")

    def add_comp(self, comp):
        self.comp.append(comp)
        log("INF", f"Изменен объект {self.name}")

    def del_comp(self, comp):
        for i in self.comp:
            if comp in i:
                self.comp.remove(i)
        log("INF", f"Изменен объект {self.name}")

    def print_comp(self):
        print('====Composition====')
        for i in self.comp:
            print(i)
        log("PRI", f"Взаимодействие с информацией объекта {self.name}")

    def __str__(self):
        log("PRI", f"Взаимодействие с информацией объекта {self.name}")
        return f'{self.name}, {self.weight} g., {self.price} RUB, ({self.cooking_time} min)'


if __name__ == "__main__":
    steak = Food('Steak', 400, 250, 10, ['meat', 'salt', 'sauce'])
    steak.print_comp()
    steak.add_comp('lemon juice')
    steak.print_comp()
    steak.del_comp('salt')
    steak.print_comp()
    steak.new_comp(['meat', 'sea salt', 'paper'])
    steak.print_comp()
    print()
    print(steak)
    steak.change_time(9)
    print(steak)
