"""Упражнение 6. Налоги и чаевые"""
order_cost = float(input('Введите стоимость заказа: '))
tax = round(order_cost * 0.13, 2)
tips = round(order_cost * 0.18, 2)
print(f'Налог: {tax}, Чаевые: {tips}, Итоговая стоимость: {
      round(order_cost + tax + tips)}')
