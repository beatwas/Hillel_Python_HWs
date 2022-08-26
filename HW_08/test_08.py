"""
Дана строка (большАя строка, лучше взять на английском). Выведите слово, которое в этой строке встречается чаще всего. Если таких слов несколько, выведите последнее.

Задачу необходимо решить с использованием словаря.
"""

import re


def frequently_repeated_word(txt):
    lst = re.split("[, \-!?:]+", txt)
    dct = dict()

    max_num = 0
    rez = string

    for item in lst:
        if item not in dct:
            dct[item] = 1
        elif item in dct:
            dct[item] += 1
            if dct[item] >= max_num:
                max_num = dct[item]
                rez = item
    return rez


string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra venenatis tortor, vitae accumsan " \
         "elit maximus eget. Vivamus posuere ornare enim, sit amet euismod turpis interdum in. Ut sollicitudin eget " \
         "nunc ac mattis. Nunc sit amet feugiat metus. Nulla facilisi. Aenean sapien eros, hendrerit sed pharetra " \
         "vel, placerat eget ante. Vivamus ligula orci, accumsan quis iaculis at, feugiat ac risus. Vivamus suscipit " \
         "lorem ut massa sagittis auctor. Fusce consequat sem eget placerat gravida. Etiam condimentum neque ex, " \
         "aliquet congue libero fermentum non. Curabitur tincidunt sapien sem, non dignissim sem feugiat sed. Donec " \
         "tempor nibh sit amet felis cursus, eget sagittis purus pulvinar. Nullam convallis leo purus, "

print(frequently_repeated_word(string))
