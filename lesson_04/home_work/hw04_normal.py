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
"""lst2 = []
for el in range(3, len(str) - 3):
    if """



print("Способ 2: без re - ", )

print("Задача 2 решена", "_"*25, "\n")

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import os
import random

"""path = os.path.join("home_work", "number.txt")
with open(path, 'w', encoding = 'UTF-8') as f:
    print(f.readlines())"""
lst2 = [random.randint(0, 9) for _ in range(2500)]
str2 = list(map(str, lst2))
print(str2)
str3 = "".join(i for i in str2)
print(str3)

file = open("number.txt", "w")
file.write(str3)
file.close()

print("Задача 3 решена", "_"*25, "\n")