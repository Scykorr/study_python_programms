"""Упражнение 13. Размен"""
change_sum = int(input('Введите сумму сдачи: '))
coins = []
toonie = coins.append(('toonie', change_sum // 200))
loonie = coins.append(('loonie', (change_sum % 200) // 100))
cents_25 = coins.append(('25 cents', (change_sum % 200 % 100) // 25))
cents_10 = coins.append(('10 cents', (change_sum % 200 % 100 % 25) // 10))
cents_5 = coins.append(('5 cents', (change_sum % 200 % 100 % 25 % 10) // 5))
cents_1 = coins.append(
    ('1 cents', (change_sum % 200 % 100 % 25 % 10 % 5) // 1))
for el in coins:
    if el[1] != 0:
        print(f'{el[0]}: {el[1]}')
