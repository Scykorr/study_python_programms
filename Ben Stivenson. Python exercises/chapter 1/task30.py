"""Упражнение 30. Цельсий в Фаренгейт и Кельвин"""


def get_temperature(temperature: float) -> None:
    print(f'Температура в Фаренгейтах: {(temperature * 9 / 5) + 32}')
    print(f'Температура в Кельвинах: {temperature + 273.15}')


if __name__ == '__main__':
    inp_temperature = float(input('Введите температуру в градусах цельсия: '))
    get_temperature(temperature=inp_temperature)
