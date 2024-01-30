"""Упражнение 5. Сдаем бутылки"""
little_bottle = int(
    input('Введите количество бутылок объемом меньше или равные 1л.: '))
big_bottle = int(input('Введите количество бутылок объемом больше 1л.: '))
result_price = round(little_bottle * 0.1 + big_bottle * 0.25, 2)
print(f'Итоговая сумма: {result_price}$')
