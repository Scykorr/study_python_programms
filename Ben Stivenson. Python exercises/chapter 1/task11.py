"""Упражнение 11. Потребление топлива"""
miles_per_gallon = float(
    input('Введите показатель потребляния топлива США\nМиль на галлон: '))
liters_per_hundred_kilometers = round(
    3.78541 * 100 / (miles_per_gallon * 1.60934), 3)
print(f'Показатель потребления топлива Канады\nЛитров на 100км: {
      liters_per_hundred_kilometers}')
