from menu import Menu
from drink import Drink
from food import Food
import pickle

if __name__ == "__main__":
    menu = pickle.load(open("menu-dump.pkl", "rb"))
    print(menu)
