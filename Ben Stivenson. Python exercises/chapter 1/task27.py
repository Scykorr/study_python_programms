"""Упражнение 27. Когда Пасха?"""
from math import floor


def get_main_date(year):
    a = year % 19
    b = floor(year / 100)
    c = year % 100
    d = floor(b / 4)
    e = b % 4
    f = floor((b + 8) / 25)
    g = floor((b - f + 1) / 3)
    h = (19 * a + b - d - g + 15) % 30
    i = floor(c / 4)
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = floor((a + 11 * h + 22 * l) / 451)
    result_month = (h + l + 7 * m + 114) / 31
    result_day = 1 + (h + l + 7 * m + 114) % 31
    print(f'Месяц пасхи:{result_month:02}.День пасхи: {result_day:02}')


if __name__ == '__main__':
    inp_year = int(input('Введите год: '))
    get_main_date(year=inp_year)
