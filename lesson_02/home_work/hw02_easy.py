__author__ = "Стиврина Мария"

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

list = ["яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз",
        "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз", "яблоко", "банан", "киви", "арбуз"]
i = 1
j = 0

for fruit in list:
    j = str(i)
    if len(j) == 1:
        print('{}. {:>10}'.format(i, fruit))
        i = i + 1
    elif len(j) == 2:
        print('{}. {:>9}'.format(i, fruit))
        i = i + 1
    else:
        print('{}. {:>8}'.format(i, fruit))
        i = i + 1

print("Задача 1 решена", "_"*25, "\n")


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random
import math

print("Здравствуйте! Мы сейчас будем создавать списки для решения поставленной задачи")

n = int(input("Введите желаемое количество элементов в первом списке: "))
m = int(input("Введите желаемое количество элементов во втором списке: "))
list1 = []
list2 = []
spisok = []

for elem in range(n):
    list1.append(random.randint(0, 10))

for elem in range(m):
    list2.append(random.randint(0, 10))

print("Первый список: ", list1)
print("Второй список: ", list2)

for elem in list1:
    if elem not in list2:
        spisok.append(elem)

print("Результирующий список = ", spisok)
print("Задача 2 решена", "_"*25, "\n")

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("Здравствуйте! Мы сейчас будем создавать список для решения поставленной задачи")

b = int(input("Введите желаемое количество элементов в первом списке: "))
list3 = []
list4 = []
i = 0

for elem in range(b):
    list3.append(random.randint(0, 100))

print("Полученный список: ", list3)

for elem in list3:
    if list3[i] % 2 == 0:
        list4.append(list3[i] / 4)
        i += 1
    else:
        list4.append(list3[i] * 2)
        i += 1

print("Новый список: ", list4)
print("Задача 3 решена", "_"*25, "\n")