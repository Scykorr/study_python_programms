"""Упражнение 6. Налоги и чаевые"""
def count_tax_and_tips(order_cost: float) -> None:
      tax = round(order_cost * 0.13, 2)
      tips = round(order_cost * 0.18, 2)
      print(f'Налог: {tax}, Чаевые: {tips}, Итоговая стоимость: {round(order_cost + tax + tips)}')


if __name__ == '__main__':
      order_cost = float(input('Введите стоимость заказа: '))
      count_tax_and_tips(order_cost=order_cost)