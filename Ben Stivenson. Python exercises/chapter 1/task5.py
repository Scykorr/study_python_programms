"""Упражнение 5. Сдаем бутылки"""
def get_money_for_bottle(little_bottle: int, big_bottle: int) -> None:
    print(f'Итоговая сумма: {round(little_bottle * 0.1 + big_bottle * 0.25, 2)}$')


if __name__ == '__main__':
    little_bottle = int(
    input('Введите количество бутылок объемом меньше или равные 1л.: '))
    big_bottle = int(input('Введите количество бутылок объемом больше 1л.: '))
    get_money_for_bottle(little_bottle=little_bottle, big_bottle=big_bottle)
