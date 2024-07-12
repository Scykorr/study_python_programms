from math import fmod

russian_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
english_letters = 'abcdefghijklmnopqrstuvwxyz'


def cesar_cipher(string, direction, step, language):
    new_string = ''
    if direction == '-':
        language = language[::-1]
    for el in string:
        if el.isalpha():
            new_el = language[(language.find(el.lower()) + int(step)) % len(language)]
        else:
            new_el = el
        if el.isupper():
            new_el = new_el.upper()
        new_string += new_el
    return new_string


# inp_string = input('Введите текст: ')
# inp_direction = input('Введите направление (+/-):')
# inp_step = input('Введите шаг: ')
# input_lang = input('Введите язык (ru/en): ')
# if input_lang == 'ru':
#     input_lang = russian_letters
# elif input_lang == 'en':
#     input_lang = english_letters
# # print(cesar_cipher(string=inp_string, direction=inp_direction, step=inp_step, language=input_lang))
# for index in range(26):
#     inp_string = 'Hawnj pk swhg xabkna ukq nqj.'
#     inp_direction = '+'
#     inp_step = index
#     input_lang = english_letters
#     print(cesar_cipher(string=inp_string, direction=inp_direction, step=inp_step, language=input_lang))

inp_string = input('Введите текст: ')
inp_lang = english_letters
for el in inp_string.split():
    inp_step = len(el)

