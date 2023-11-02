from item import Item
from log import *


class Drink(Item):

    def __init__(self, name, price, volume=0, menu="", comp=None):
        super().__init__(name, price)
        self.volume = volume
        self.menu = menu
        self.comp = comp

    def add(self, ing="?", volume=0):
        self.comp[ing] = volume
        log("INF", f"Изменен объект {self.name}")

    def delete(self, ing="?"):
        try:
            self.comp.pop(ing)
            log("INF", f"Изменен объект {self.name}")
        except KeyError:
            print("Incorrect ingredient!")
            log("ERR", f"Ошибка при изменении объекта {self.name}")

    def print_comp(self):
        print('====Composition====')
        t_comp = [(ing, self.comp[ing]) for ing in self.comp]
        t_comp.sort(key=lambda x: x[1], reverse=True)
        for ing in t_comp:
            print(ing[0], " - ", ing[1])
        log("PRI", f"Взаимодействие с информацией объекта {self.name}")

    def __str__(self):
        log("PRI", f"Взаимодействие с информацией объекта {self.name}")
        return f'{self.name} from {self.menu} menu section, {self.volume} ml for {self.price} RUB'


if __name__ == "__main__":
    cola = Drink('🥤Cola🥤', 100, 250, "Soda", {'Sugar': 60, 'Water': 140})
    cola.print_comp()
    cola.add('Acid', 10)
    cola.print_comp()
    cola.delete('Sugar123')
    cola.delete('Sugar')
    cola.print_comp()
    print(cola)
