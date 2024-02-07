"""Упражнение 25. Единицы времени (снова)"""


def get_time_from_sec(seconds: int) -> None:
    days = seconds // (24 * 3600)
    hours = (seconds - days * 24 * 3600) // 3600
    minutes = (seconds - days * 24 * 3600 - hours * 3600) // 60
    seconds = seconds - days * 24 * 3600 - hours * 3600 - minutes * 60
    print(f'Время: {days}:{hours:02}:{minutes:02}:{seconds:02}')


if __name__ == '__main__':
    inp_seconds = int(input('Введите количество секунд: '))
    get_time_from_sec(seconds=inp_seconds)
