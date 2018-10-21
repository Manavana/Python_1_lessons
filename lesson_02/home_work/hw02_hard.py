__author__ = "Стиврина Мария"

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y
#
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# подсказка: x у вас уже есть, остается с помощью срезов получить значения k и b,
# а затем вевести итоговый результат: print('y = {}'.format(k * x + b))


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:

# 1. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа (числа) для дня, 2 - для месяца, 4 - для года)

# 2. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 3. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 4. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999

"""
# Пример корректной даты
date = '01.11.1985'
# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'
"""