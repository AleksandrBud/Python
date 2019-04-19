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
        #Расчет вероятности, пустая клетка или заполненая
        self.is_digit = False
        if random.random() > (5 - count_digit)/(10 - col):
            self.numb = 0
        else:
            self.is_digit = True
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
            return ' {}'.format(self.numb)


class LineCard(object):

    def __init__(self):
        self.line = []
        self.col_dig = 0
        for i in range(1, 10):
            self.line.append(Digit(i, self.col_dig))
            if self.line[i - 1].numb != 0:
                self.col_dig = self.col_dig + 1

    def print_line(self):
        o_str = ''
        for i in range(0, 9):
            o_str = o_str + self.line[i].print_digit()
        return o_str


class LotoCard(object):

    def __init__(self):
        self.header = '------ Ваша карточка -----'
        self.line1 = LineCard()
        self.line2 = LineCard()
        self.line3 = LineCard()
        self.footer = '--------------------------'

    def print_card(self):
        print(self.header)
        print(self.line1.print_line())
        print(self.line2.print_line())
        print(self.line3.print_line())
        print(self.footer)


class Game(object):
    def __init__(self):
        self.my_card = LotoCard()
        self.ii_card = LotoCard()

    def print_card(self):
        self.my_card.print_card()
        self.ii_card.print_card()


g1 = Game()
g1.print_card()
