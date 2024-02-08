"""Упражнение 28. Индекс массы тела"""


def get_body_index(weight: float, height: float) -> None:
    bmi = weight / pow(height, 2)
    category = ''
    if bmi < 18.5:
        category = 'Недостоточный вес'
    elif 18.5 <= bmi <= 24.9:
        category = 'Нормальный вес'
    elif 25 <= bmi <= 29.9:
        category = 'Избыточный вес'
    else:
        category = 'Ожирение'
    print(f'ИМТ: {bmi}. {category}.')


if __name__ == '__main__':
    inp_weight = float(input('Введите Ваш вес в киллограммах: '))
    inp_height = float(input('Введите Ваш рост в метрах: '))
    get_body_index(weight=inp_weight, height=inp_height)
