"""Упражнение 4. Площадь садового участка"""
place_length = float(input('Введите длину участка в футах: '))
place_width = float(input('Введите ширину участка в футах: '))
print(f'Площадь садового участка в акрах: {
      round((place_length * place_width) / 43560, 2)}')
