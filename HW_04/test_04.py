"""
  Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся
записи о номере заказа, названии книги, количестве и стоимости одной книги, как
представлено ниже, в таблице.
+--------------+------------------------------------+----------+----------------+
| Order Number |       Book Title and Author        | Quantity | Price per Item |
+--------------+------------------------------------+----------+----------------+
|        34587 | Learning Python, Mark Lutz         |        4 |          40.95 |
|        98762 | Programming Python, Mark Lutz      |        5 |          56.80 |
|        77226 | Head First Python, Paul Barry      |        3 |          32.95 |
|        88112 | Einfuhrung in Python3, Bernd Klein |        3 |          24.99 |
+--------------+------------------------------------+----------+----------------+
Напишите программу на Python, которая на вход получает список списков:
[
  [34587, 'Learning Python, Mark Lutz', 4, 40.95],
  [98762, 'Programming Python, Mark Lutz', 5, 56.80],
  [77226, 'Head First Python, Paul Barry', 3, 32.95],
  [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость заказа должна быть увеличена на $10, если она
меньше $100. Программа должна использовать lambda, map, однострочный if, round и list.
Решение задачи должно быть выполнено в ОДНУ СТРОКУ!
"""

ent = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
rez = list(map(lambda item: (item[0], round(int(item[2]) * ((float(item[3]) * 10) if float(item[3]) < 100 else float(item[3]) * 10), 2)), ent))

print(rez)