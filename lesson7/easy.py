# !/usr/bin/python3

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
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random
import os
from typing import List


class Digit(object):

    def __init__(self, col, count_digit):
        #Расчет вероятности, пустая клетка или заполненаяgs]
        if random.random() > (5 - count_digit)/(10 - col):
            self.numb = 0
        else:
            a = 0 + (col - 1) * 10
            b = 9 + (col - 1) * 10
            if a == 0:
                a = 1
            if b == 89:
                b = 90
            self.numb = random.randint(a, b)

    def print_digit(self):
        if self.numb == 0:
            return '   '#пустая ячейка
        elif self.numb == -1:
            return ' - '#цифра была
        elif self.numb > 9:
            return ' {}'.format(self.numb)
        else:
            return ' {} '.format(self.numb)


class LineCard(object):

    def __init__(self, ex_digits):
        self.line = []
        self.line.__len__()
        self.col_dig = 0
        for i in range(1, 10):
            digit = Digit(i, self.col_dig)
            while digit in ex_digits:
                digit = Digit(i, self.col_dig)

            self.line.append(digit)
            if self.line[i - 1].numb != 0:
                self.col_dig = self.col_dig + 1

    def print_line(self):
        o_str = ''
        for i in range(0, 9):
            o_str = o_str + self.line[i].print_digit()
        return o_str

    def get_digits(self):
        return [i.numb for i in self.line]

    def rem_dig(self, i_rem_dig):
        for i in range(0, 9):
            if i_rem_dig == self.line[i].numb:
                self.line[i].numb = -1
                break
        pass

class LotoCard(object):

    def __init__(self):
        self.header = '---------------------------'
        self.card_digits = []
        self.line1 = LineCard(self.card_digits )
        self.card_digits = self.line1.get_digits()
        self.line2 = LineCard(self.card_digits )
        self.card_digits = self.card_digits + self.line2.get_digits()
        self.line3 = LineCard(self.card_digits )
        self.card_digits = self.card_digits + self.line3.get_digits()
        self.footer = '---------------------------'

    def print_card(self):
        print(self.header)
        print(self.line1.print_line())
        print(self.line2.print_line())
        print(self.line3.print_line())
        print(self.footer)

    def remove_digit(self, rem_dig):
        self.card_digits.remove(rem_dig)
        self.line1.rem_dig(rem_dig)
        self.line2.rem_dig(rem_dig)
        self.line3.rem_dig(rem_dig)

class Game(object):
    def __init__(self):
        self.collections_digit = [i for i in range(1, 91)]
        self.name = input('Введите имя первого игрока: ')
        self.my_card = LotoCard()
        self.name_ii = input('Введите имя второго игрока: ')
        self.ii_card = LotoCard()

    def check_digit_in_card(self, card, search_digit, otvet):
        if search_digit in card.card_digits and otvet == 'y':
            #Зачеркнуть цифру
            card.remove_digit(search_digit)
            return True
        elif search_digit not in card.card_digits and otvet == 'n':
            return True
        else:
            print('{} проиграл'.format(self.name))
            return False

    def print_card(self):
        while True:
            print(self.name)
            self.my_card.print_card()
            print()
            print(self.name_ii)
            self.ii_card.print_card()
            print()
            num = random.randint(1, 91)
            while num not in self.collections_digit:
                num = random.randint(1, 91)
            self.collections_digit.remove(num)#Удаляем боченок из списка
            print(num)
            print()
            inp = input('{} зачеркнуть цифру? (y/n)'.format(self.name))
            if not self.check_digit_in_card(self.my_card, num, inp):
                break
            if self.my_card.card_digits.__len__() <= 0:
                print('{} победил!')
                break
            inp = input('{} зачеркнуть цифру? (y/n)'.format(self.name_ii))
            if not self.check_digit_in_card(self.ii_card, num, inp):
                break
            if self.ii_card.card_digits.__len__() <= 0:
                print('{} победил!')
                break
            if self.collections_digit.__len__() <= 0:
                print('Игра окончена боченков не осталось')
                break

g1 = Game()
g1.print_card()
