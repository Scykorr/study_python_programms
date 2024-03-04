"""Упражнение 19. Свободное падение"""
from math import sqrt


def calc_free_fall_speed(inp_height: float) -> None:
    print(
        f'Скорость во время соприкосновения с землей: {round(sqrt(2 * 9.8 * inp_height), 3)}')


if __name__ == '__main__':
    inp_height = float(input('Введите высоту в метрах: '))
    calc_free_fall_speed(inp_height=inp_height)
