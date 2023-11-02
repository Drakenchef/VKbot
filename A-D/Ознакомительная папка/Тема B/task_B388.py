# Написать функцию commas, которая преобразует заданное число в строку с добавлением
# запятых для удобства чтения. Число должно быть округлено до 3 значащих цифр,
# а запятые следует добавлять с интервалом в три цифры перед десятичной точкой.
#
# Примеры:
# commas(100.2346) ==> "100.235"
# commas(-1000000.123) ==> "-1,000,000.123"


import traceback


def commas(number):
    number = round(number, 3)
    if number % 1 == 0:
        number = int(number)
    return f"{number:,}"



# Тесты
try:
    assert commas(1) == "1"
    assert commas(1000) == "1,000"
    assert commas(100.2346) == "100.235"
    assert commas(1000000000.23) == "1,000,000,000.23"
    assert commas(-999.9999) == "-1,000"
    assert commas(-1234567.0001236) == "-1,234,567"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")