"""Упражнение 14. Рост"""
input_height_foot = int(input('Введите количество футов в Вашем росте: '))
input_height_inch = int(input('Введите количество дюймов в Вашем росте: '))
height_centimeters = (input_height_foot * 12 + input_height_inch) * 2.54
print(f'Ваш рост в сантиметрах: {height_centimeters}')
