"""Упражнение 13. Размен"""

def exchange_coins(change_sum):
    coins = []
    coins.append(('toonie', change_sum // 200))
    coins.append(('loonie', (change_sum % 200) // 100))
    coins.append(('25 cents', (change_sum % 200 % 100) // 25))
    coins.append(('10 cents', (change_sum % 200 % 100 % 25) // 10))
    coins.append(('5 cents', (change_sum % 200 % 100 % 25 % 10) // 5))
    coins.append(
        ('1 cents', (change_sum % 200 % 100 % 25 % 10 % 5) // 1))
    for el in coins:
        if el[1] != 0:
            print(f'{el[0]}: {el[1]}')


if __name__ == '__main__':
    change_sum = int(input('Введите сумму сдачи: '))
    exchange_coins(change_sum=change_sum)
