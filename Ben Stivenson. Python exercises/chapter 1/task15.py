"""Упражнение 15. Расстояние"""


def calc_distance(inp_length: float) -> None:
    print(
        f'Расстояние в дюймах: {inp_length * 12}\nРасстояние в ярдах: {inp_length * 0.33}\nРасстояние в милях: {inp_length * 0.00018939375}')


if __name__ == '__main__':
    inp_length = float(input('Введите расстояние в футах: '))
    calc_distance(inp_length=inp_length)
