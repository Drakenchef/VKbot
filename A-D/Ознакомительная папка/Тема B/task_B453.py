"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

def wiki_function():
    f = open("AB/B453.txt", "r")
    lines = []
    for line in f:  # добавляем все не пусстые строки
        if line != '' and line != '\n':
            lines.append(line)
    f.close()

    linesf = []

    for line in lines:  # Оставляем только буквы и пробелы
        linef = ""
        for symb in line:
            if symb.isalpha() or symb == ' ':
                linef = linef + symb
        linesf.append(linef)

    text = ' ' + ' '.join(linesf) + ' '     # Добавляем все в одну строку

    words = text.split()
    words_count = {key:words.count(key) for key in words}   # Создаем словарь с кол-вом слов

    words_count_t = [(key, words_count[key]) for key in words_count]    # Выводим 5 самых популярных слов
    words_count_t.sort(key = lambda x: (x[1], x[0]))
    words_count_t.reverse()
    for i in range(10):
        print(i+1, 'place:', words_count_t[i][0], '-', words_count_t[i][1], 'times')

    for i in range(10): # Заменияем все эти слова на слово PYTHON
        text = text.replace(' ' + words_count_t[i][0] + ' ', ' PYTHON ')


    f = open('AB/B453-out.txt', 'w')

    words = text.split()
    current_line = ''

    for word in words:
        if len(current_line) + len(word) + 1 > 100:
            f.write(current_line + '\n')
            current_line = ""

        if current_line == "":
            current_line += word
        else:
            current_line += " " + word

    if current_line != "":
        f.write(current_line)



    return 1


# Вызов функции
wiki_function()