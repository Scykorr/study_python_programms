"""Упражнение 19. Свободное падение"""
from math import sqrt
inp_height = float(input('Введите высоту в метрах: '))
ending_speed = round(sqrt(2 * 9.8 * inp_height), 3)
print(f'Скорость во время соприкосновения с землей: {ending_speed}')