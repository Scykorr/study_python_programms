"""Упражнение 34. Вчерашний хлеб"""


def count_price(bread_amount: int):
    common_price = 3.49
    new_price = round(3.49 * 0.6, 2)
    result_cost = round(bread_amount * new_price, 2)
    print(f'--------------------------------------\n'
          f'Цена свежего хлеба: {common_price}\n'
          f'Цена вчерашнего хлеба: {new_price}\n'
          f'Стоимость {bread_amount} буханок вчерашнего хлеба: {result_cost}')


if __name__ == '__main__':
    inp_bread_amount = int(input('Введите количество буханок хлеба: '))
    count_price(bread_amount=inp_bread_amount)
