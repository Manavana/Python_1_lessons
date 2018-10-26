__author__ = "Стиврина Мария"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(x, y):
    fibonacci = [0, 1, 1]
    i = 3
    while len(fibonacci) <= y:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        i += 1
    return fibonacci[x:y + 1]

n = int(input("Введите элемент, от которого необходимо вывести ряд Фибоначчи: "))
m = int(input("Введите элемент, до которого необходимо вывести ряд Фибоначчи: "))

if n < m:
    print("Полученный ряд Фибоначчи: ", fibonacci(n, m))
else:
    print("Некорректно введен диапазон выводимых элементов")

print("Задача 1 решена", "_"*25, "\n")

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

import random

def sorting(num):
    lst = []
    for elem in range(n):
        lst.append(random.randint(0, 10))

    i = 1
    while i < len(lst):
         for el in range(len(lst) - i):
              if lst[el] > lst[el + 1]:
                   lst[el], lst[el + 1] = lst[el + 1], lst[el]
         i += 1
    return lst

n = int(input("Введите желаемое количество элементов в списке: "))

print("Отсортированный список: ", sorting(n))
print("Задача 2 решена", "_"*25, "\n")

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, list):
    lst = []
    if func == 1:
        for el in list:
            if el > 5:
                lst.append(el)
        return lst
    elif func == 2:
        for el in list:
            if el < 0:
                lst.append(el)
        return lst
    else:
        return list

import random

list1 = []
n = int(input("Введите желаемое количество элементов в списке: "))
for el in range(n):
    list1.append(random.randint(-10, 10))

m = int(input("Какой функцией Вы хотели бы отфильтровать элементы списка? Нажмите 1 если x > 5, нажмите 2 если x < 0 "))

if m == 1 or m == 2:
    print("Отфильтрованный список: ", my_filter(m, list1))
else:
    print("Я такой функции не знаю. Держите исходный список: ", list1)

print("Задача 3 решена", "_"*25, "\n")

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print("Задача 4 решена", "_"*25, "\n")