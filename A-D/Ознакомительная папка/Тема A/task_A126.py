# Написать функцию max_multiple(divisor, bound), которая определяет максимальное N,
# которое делится на divisor, меньше или равно bound и больше нуля
#
# Примеры:
# max_multiple(2,7) ==> 6
# max_multiple(10,50) ==> 50

import traceback


def max_multiple(divisor, bound):
    res = 0 
    for i in range(bound+1):
        if i % divisor == 0:
            res = i
    return res


# Тесты
try:
    assert max_multiple(7, 100) == 98
    assert max_multiple(37, 100) == 74
    assert max_multiple(4, 1) == 0
    assert max_multiple(1, 1) == 1
    assert max_multiple(7,17) == 14
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")