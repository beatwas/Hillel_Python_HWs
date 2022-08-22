"""
1. В текстовый файл (файл прилагается), построчно записаны имя и
фамилия учащихся класса и их оценки.
 Вывести на экран всех учащихся, чей средний балл меньше 5, также
посчитать и вывести средний балл по классу. Так же, записать в новый
файл всех учащихся в формате "Фамилия И. Ср. балл":
 Говорухи А. 5.83
 Петров В. 4.92
 Варфаломеев Г. 5.92
 Тюльпанов И. 4.08
 Муромцев И. 5.42
 Бессмертный К. 5.5
 Мухин М. 6.92
 Мартынова М. 6.08
 Николаев П. 5.17
 Гусева Г. 5.83
 Тереньтьев С. 6.42
 Трердолобов С. 5.33
 Выравнивание колонок - ОБЯЗАТЕЛЬНО!
"""

from statistics import mean

names = list()
av_marks = list()


with open("src_14.txt", "r", encoding="utf8") as file:
    contents = file.readlines()
    for item1 in contents:
        a = item1.split()
        names.append(a[1] + " " + a[0][0] + ".")

        c = 0
        s = 0
        for item2 in a:
            if c > 1:
                s += int(item2)
            c += 1
        av_marks.append(round(s / (c - 2), 2))


print("Students with GPA less than 5:")
c = 0
for item in av_marks:
    if item < 5:
        print(names[c])
    c += 1
print()

print("Average score by class: " + str(round(mean(av_marks), 2)))

print()
f_tb = list()

c = 0
for item in names:
    f_tb.append([names[c], av_marks[c]])
    c += 1


with open("result.txt", "w") as file:
    for item in f_tb:
        file.write("{:<15}{:>10}".format(*item) + "\n")
