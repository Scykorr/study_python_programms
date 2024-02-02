"""Упражнение 11. Потребление топлива"""
def measure_gas_value(miles_per_gallon: float) -> None:
    liters_per_hundred_kilometers = round(3.78541 * 100 / (miles_per_gallon * 1.60934), 3)
    print(f'Показатель потребления топлива Канады\nЛитров на 100км: {liters_per_hundred_kilometers}')


if __name__ == '__main__':
    miles_per_gallon = float(input('Введите показатель потребляния топлива США\nМиль на галлон: '))
    measure_gas_value(miles_per_gallon=miles_per_gallon)