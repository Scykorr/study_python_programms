"""Упражнение 17. Теплоемкость"""
from typing import Final
inp_weight = float(input('Введите массу воды: '))
inp_delta_temp = float(input('Введите разницу температур: '))
heat_capacity: Final = 4.186
req_energy = inp_weight * heat_capacity * inp_delta_temp
print(f'Общее количество требуемой энергии: {req_energy}')
cost_energy = 2.77778e-07 * req_energy * 8.9
print(f'Итоговая стоимость: {cost_energy} центов')
