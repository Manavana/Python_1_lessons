# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

# способ 1: с помощью re
string = "mtMmEZUOmcq"
pattern = "[a-z]?[a-z]*[a-z]"

print("Способ 1: с помощью re - ", re.findall(pattern, string))

# способ 2: без re
lst = "".join(i for i in string if i.islower())
lst1 = [i for i in string if i.islower()]

print("Способ 2: без re - ", lst, "\n", lst1)

print("Задача 1 решена", "_"*25, "\n")

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
import re

# способ 1: с помощью re
str1 = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
pttrn = "[a-z]{2}([A-Z]+)[A-Z]{2}"

print("Способ 1: с помощью re - ", re.findall(pttrn, str1))

# способ 2: без re
low_reg = 0
up_reg = 0

"""for el in str1:
    if el.islower():
        low_reg += 1
        if low_reg == 2 and 
    else:
        up_reg += 1"""
up_reg_list = []
str_1 = str1[3:]
print(str_1)
for el in range(len(str_1)):
    if str_1[el].islower():
        low_reg += 1
        """if low_reg >= 2 and up_reg >= 3:
            up_reg_list.append(str_1[el])
            low_reg = 0
            up_reg = 0"""
    else:
        up_reg += 1
        if low_reg >= 2 and up_reg == 4:
            up_reg_list.append(str_1[el - 3])
            up_reg_list.append(str_1[el - 2])
            low_reg = 0
            up_reg = 0

print("Способ 2: без re - ", up_reg_list)

print("Задача 2 решена", "_"*25, "\n")

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import os
import random

"""lst2 = [random.randint(0, 2) for _ in range(10)]
str2 = list(map(str, lst2))
print(str2)
str3 = "".join(i for i in str2)
print(str3) <------ Для тестирования алгоритма нахождения наибольшей последовательности на меньшей выборке чисел для 
большей наглядности"""

lst2 = [random.randint(0, 9) for _ in range(2500)]
str2 = list(map(str, lst2))
print(str2)
str3 = "".join(i for i in str2)
print(str3)

file = open("number.txt", "w")
file.write(str3)
file.close()

with open("number.txt", 'r', encoding = 'UTF-8') as file:
    line = (file.read())

num = ""
num_max = ""
j = 1
jmax = 0

for el in range(len(line) - 1):
    if line[el] == line[el + 1]:
        num = line[el]
        j += 1
        if jmax < j:
            jmax = j
            num_max = num
    else:
        if jmax < j:
            jmax = j
            num_max = num
            j = 1
            num = ""
        else:
            j = 1

if jmax == 1:
    print("Повторяющихся цифр в процессе чтения файла не попадалось")
else:
    print("Самая длинная последовательность состоит из {} одинаковых цифр, повторяющееся число {}".format(jmax, num_max))

print("Задача 3 решена", "_"*25, "\n")