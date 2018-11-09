__author__ = "Стиврина Мария"

#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random

class Card:
    def __init__(self):
        self.card = []

    def make_card(self):
        intermediate_list = []

        # Прописываю в первом цикле for генерацию значений для карточки больше 15 + отбираю неповторяющиеся
        for el in range(20):
            element = random.randint(1, 90)
            if element not in intermediate_list:
                intermediate_list.append(element)

        # отбираю нужное количество неповторяющихся значений для карточки
        self.card = random.sample(intermediate_list, 15)
        #print(self.card)
        self.line1 = self.card[:5]
        self.line1.sort()
        self.line2 = self.card[5:10]
        self.line2.sort()
        self.line3 = self.card[10:]
        self.line3.sort()

    def get_len_card(self):
        return len(self.card)

    def __str__(self):
        return """{}  {}  {}  {}  {}
{}  {}  {}  {}  {}
{}  {}  {}  {}  {}""".format(self.line1[0], self.line1[1], self.line1[2], self.line1[3], self.line1[4],
                             self.line2[0], self.line2[1], self.line2[2], self.line2[3], self.line2[4],
                             self.line3[0], self.line3[1], self.line3[2], self.line3[3], self.line3[4])

    def compare_numbers(self, number):
        for num in self.card:
            if num == number:
                return True
        return False

class Barrel:
    def __init__(self):
        self.barrel_in_bag = []
        self.barrel_dropped = []

    def shuffle_bag(self):
        # накидали бочонков в мешок и тщательно перемешали
        self.barrel_in_bag = [i for i in range(1, 91)]
        random.shuffle(self.barrel_in_bag)

    def get_barrel(self):
        # вытянули случайный бочонок из мешка
        self.barrel = random.choice(self.barrel_in_bag)
        # скинули его в другой мешок
        self.barrel_dropped.append(self.barrel)
        self.barrel_in_bag.pop(self.barrel_in_bag.index(self.barrel))
        print("\nНовый бочонок: ", self.barrel, "(осталось {})".format(len(self.barrel_in_bag)))
        return self.barrel

my_card = Card()
my_card.make_card()

computer_card = Card()
computer_card.make_card()

bag_with_barrel = Barrel()
bag_with_barrel.shuffle_bag()

while my_card.get_len_card() > 0 and computer_card.get_len_card() > 0:
    if my_card.get_len_card() == 0:
        print("$$$ Поздравляем! Вы выиграли джекпот! $$$")
        break

    if computer_card.get_len_card() == 0:
        print("Сегодня не Ваш день...")
        break

    number = bag_with_barrel.get_barrel()

    print("\n------ Моя карточка ------")
    print(my_card)
    print("--------------------------")

    print("\n--- Карточка компьютера --")
    print(computer_card)
    print("--------------------------")

    answer = input("Зачеркнуть цифру? (y/n)")

    if my_card.compare_numbers(number) == True and answer == "y":
        continue
    elif my_card.compare_numbers(number) == True and answer == "n":
        print("Вы ошиблись. Такая цифра есть у Вас в карточке. К сожалению, игра окончена")
        break
    elif my_card.compare_numbers(number) == False and answer == "y":
        print("Вы ошиблись. Такой цифры нет у Вас в карточке. К сожалению, игра окончена")
        break
    elif my_card.compare_numbers(number) == False and answer == "n":
        continue
    else:
        print("Я не понял Ваш ответ. Извините, но это проигрыш")
        break
