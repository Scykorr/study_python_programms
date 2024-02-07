"""Упражнение 24. Единицы времени"""


def get_seconds(days: int,
                hours: int,
                minutes: int,
                seconds: int) -> None:
    print(f'Общее количество секунд: {
          days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds}')


if __name__ == '__main__':
    inp_days = int(input('Введите количество дней: '))
    inp_hours = int(input('Введите количество часов: '))
    inp_minutes = int(input('Введите количество минут: '))
    inp_seconds = int(input('Введите количество секунд: '))
    get_seconds(days=inp_days,
                hours=inp_hours,
                minutes=inp_minutes,
                seconds=inp_seconds)
