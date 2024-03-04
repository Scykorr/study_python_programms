"""Упражнение 4. Площадь садового участка"""


def count_sqr_garden(place_length: float, place_width: float) -> None:
    print(
        f'Площадь садового участка в акрах: {round((place_length * place_width) / 43560, 2)}')


if __name__ == '__main__':
    place_length = float(input('Введите длину участка в футах: '))
    place_width = float(input('Введите ширину участка в футах: '))
    count_sqr_garden(place_length=place_length, place_width=place_width)
