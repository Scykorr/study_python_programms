"""Упражнение 29. Температура с учетом ветра"""


def get_temperature_with_wind(temperature: float,
                              wind_speed: float) -> None:
    print(f'Коэффициент охлаждения ветром: {round(13.12 + 0.6215 * temperature - 11.37 *
          pow(wind_speed, 0.16) + 0.3965 * temperature * pow(wind_speed, 0.16))}')


if __name__ == '__main__':
    inp_temperature = float(input('Введите температуру: '))
    inp_wind_speed = float(input('Введите скорость ветра: '))
    get_temperature_with_wind(
        temperature=inp_temperature, wind_speed=inp_wind_speed)
