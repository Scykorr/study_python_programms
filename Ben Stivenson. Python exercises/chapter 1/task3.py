"""Упражнение 3.Площадь комнаты"""


def count_sqr(room_length: float, room_width: float) -> None:
    print(f'Площадь комнаты: {room_length * room_width} квадратных метров')


if __name__ == '__main__':
    room_lenght = float(input('Введите длину комнаты в метрах: '))
    room_width = float(input('Введите ширину комнаты в метрах: '))
    count_sqr(room_length=room_lenght, room_width=room_width)
