__author__ = "Стиврина Мария"

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def rounding(num, sym):
    lst = []
    decimal_part = []
    int_part = []
    elem = 0
    for el in num:
        lst.append(el)
    for el in lst:
        if el is ".":
            elem = lst.index(".")
            int_part = lst[:elem + 1]
            decimal_part = lst[elem + 1:]
            if int(decimal_part[sym]) >= 5:
                decimal_part[sym - 1] = str(int(decimal_part[sym - 1]) + 1)
                if decimal_part[sym - 1] == "10":
                    decimal_part[sym - 2] = str(int(decimal_part[sym - 2]) + 1)
                    decimal_part[sym - 1] = str(int(decimal_part[sym - 1]) % 10)
                for el in decimal_part[:sym]:
                    int_part.append(el)
                return int_part
            else:
                for el in decimal_part[:sym]:
                    int_part.append(el)
                return int_part

number = input("Введите округляемое число: ")
symbol = int(input("До какого знака после запятой необходимо округлить? "))

print("Полученное число: ", rounding(number, symbol))

print("Задача 1 решена", "_"*25, "\n")

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(str):
    sum1 = int(str[0]) + int(str[1]) + int(str[2])
    sum2 = int(str[3]) + int(str[4]) + int(str[5])
    return bool(sum1 == sum2 and len(str) == 6)

ticket = input("Введите номер билета: ")

if lucky_ticket(ticket) == True:
    print("Чёрт возьми, да вы счастливчик! :)")
elif lucky_ticket(ticket) == False and len(ticket) != 6:
    print("Некорректно введен номер билета. Попробуйте еще раз")
else:
    print("К сожалению, билет оказался несчастливым :(")

print("Задача 2 решена", "_"*25, "\n")