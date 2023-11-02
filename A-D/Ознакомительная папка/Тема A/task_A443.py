# Написать функцию palindrome, которая для заданного числа num возвращает список всех числовых палиндромов,
# содержащихся в каждом номере. Массив должен быть отсортирован в порядке возрастания,
# а любые дубликаты должны быть удалены.
#
# Пример:
# palindrome(34322122)  =>  [22, 212, 343, 22122]

from itertools import groupby
import traceback


def palindrome(num):
    s = str(num)
    arr = []

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i:j+1] == s[i:j+1][::-1] and not int(s[i:j+1:]) == 0:
                arr.append(int(s[i:j+1:]))

    # for i in range(1, (len(s) // 2)+len(s)%2):
    #     for j in range(len(s), i, -1):
    #         if s[i:-j] == s[i:-j][::-1]:
    #             arr.append(int(s[i:-i]))
    arr.sort()
    new_arr = [a for a, _ in groupby(arr)]
    # print(*new_arr)
    return new_arr


# Тесты
try:
    assert palindrome(1551) == [55, 1551]
    assert palindrome(221122) == [11, 22, 2112, 221122]
    assert palindrome(10015885) == [88, 1001, 5885]
    assert palindrome(13598) == []
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
