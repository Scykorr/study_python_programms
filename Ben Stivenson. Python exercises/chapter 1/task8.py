"""Упражнение 8. Сувениры и безделушки"""
souvenir_weight = round(0.75 * int(input('Введите количество сувениров: ')), 3)
trinket_weight = round(
    0.112 * int(input('Введите количество безделушек: ')), 3)
print(f'Вес посылки: {souvenir_weight + trinket_weight}кг.')
