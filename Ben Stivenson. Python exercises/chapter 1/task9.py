"""Упражнение 9. Сложные проценты"""
initial_sum = float(
    input('Введите сумму начального депозита: ').replace(',', '.'))
for year in range(1, 4):
    initial_sum += initial_sum * 0.04
    print(f'Сумма на конец {year} года: {round(initial_sum, 2)}')
