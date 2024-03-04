"""Упражнение 9. Сложные проценты"""


def count_complex_percents(initial_sum: float) -> None:
    for year in range(1, 4):
        initial_sum += initial_sum * 0.04
        print(f'Сумма на конец {year} года: {round(initial_sum, 2)}')


if __name__ == '__main__':
    initial_sum = float(
        input('Введите сумму начального депозита: ').replace(',', '.'))
    count_complex_percents(initial_sum=initial_sum)
