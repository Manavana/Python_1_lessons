__author__ = "Стиврина Мария"

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Необходимо вывести поочередно цифры введенного пользователем числа

i = 0

a = str(input("Введите произвольное целое число: "))
b = a[i]

for b in a:
    print("- ", b)
    i += 1

print("_"*25, "\n")

 # Задача-2: Запросите у пользователя ввод двух чисел и связать значения с соответствующими переменными
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input("Введите значение переменной a: ")
b = input("Введите значение переменной b: ")

c = a
a = b
b = c

print("a = ", a, "b = ", b)
print("_"*25, "\n")

 # Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Сколько Вам лет? Ввод: "))

if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

print("_"*25, "\n")
