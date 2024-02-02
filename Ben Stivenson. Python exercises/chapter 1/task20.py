"""Упражнение 20. Уравнение состояния идеального газа"""
from typing import Final
def main(inp_P, inp_V, const_R, inp_T):
    result_n = round((inp_P * inp_V) / (const_R * inp_T), 3)
    print(f'Количество вещества: {result_n} моль') 

if __name__ == '__main__':
    inp_P = float(input('Введите давление: '))
    inp_V = float(input('Введите объем: '))
    const_R: Final = 8.314
    inp_T = float(input('Введите температуру в градусах по цельсию: ')) + 273.15
    main(inp_P, inp_V, const_R, inp_T)