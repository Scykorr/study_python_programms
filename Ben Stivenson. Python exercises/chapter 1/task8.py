"""Упражнение 8. Сувениры и безделушки"""
def count_price(souvenir_weight: float, trinket_weight: float) -> None:
    print(f'Вес посылки: {souvenir_weight + trinket_weight}кг.')

if __name__ == '__main__':
    souvenir_weight = round(0.75 * int(input('Введите количество сувениров: ')), 3)
    trinket_weight = round(0.112 * int(input('Введите количество безделушек: ')), 3)
    count_price(souvenir_weight=souvenir_weight, trinket_weight=trinket_weight)