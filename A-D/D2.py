import math


def func1(x, y, a, b):
    return (8+abs(x-y)**3)**(1/3)/(math.sqrt(x**2 + a*b*y) + 1) + 0.05 * math.log10(x)


def func2(x, y, k):
    return math.exp(-1 * k * x) * (1 + math.cos(x**3))**2 + math.tan(y) ** 2


print(func1(1, 1, 1, 1))
print(func2(1, 1, 1))
