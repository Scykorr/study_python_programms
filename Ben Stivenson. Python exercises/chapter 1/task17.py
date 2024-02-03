"""Упражнение 17. Теплоемкость"""
from typing import Final

def calc_heat_capacity(inp_weight: float, inp_delta_temp: float) -> None:
    heat_capacity: Final = 4.186
    req_energy = inp_weight * heat_capacity * inp_delta_temp
    print(f'Общее количество требуемой энергии: {req_energy}')
    cost_energy = 2.77778e-07 * req_energy * 8.9
    print(f'Итоговая стоимость: {cost_energy} центов')


if __name__ == '__main__':
    inp_weight = float(input('Введите массу воды: '))
    inp_delta_temp = float(input('Введите разницу температур: '))
    calc_heat_capacity(inp_weight=inp_weight, inp_delta_temp=inp_delta_temp)