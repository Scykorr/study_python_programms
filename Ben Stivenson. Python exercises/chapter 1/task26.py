"""Упражнение 26. Текущее время"""

from time import asctime


def get_curr_time() -> None:
    print(f'Текущее время: {asctime()}')


if __name__ == '__main__':
    get_curr_time()
