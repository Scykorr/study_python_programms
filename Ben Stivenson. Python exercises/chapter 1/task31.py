"""Упражнение 31. Единицы давления"""


def get_pressure_unit(kilo_pascals: float) -> None:
    print(f'Ваше значение в: милимметрах ртутного столба: {
          kilo_pascals * 7.50062}, атмосферах: {kilo_pascals * 0.00986923}')


if __name__ == '__main__':
    inp_kilo_pascals = float(input('Введите число килопаскалей: '))
    get_pressure_unit(kilo_pascals=inp_kilo_pascals)
