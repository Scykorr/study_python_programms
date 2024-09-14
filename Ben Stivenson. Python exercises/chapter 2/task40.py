"Упражнение 40. Громкость звука"


def check_noise(noise_level):
    if noise_level < 40:
        print('Тише некуда')
    elif noise_level == 40:
        print('Тихая комната')
    elif 40 < noise_level < 70:
        print("Значение шума между тихой комнатой и будильником")
    elif noise_level == 70:
        print('Будильник')
    elif 70 < noise_level < 106:
        print("Значение шума между будильником и газовой газонокосилкой")
    elif noise_level == 106:
        print('Газовая газонокосилка')
    elif 106 < noise_level < 130:
        print("Значение шума между газовой газонокосилкой и отбойным молотком")
    elif noise_level == 130:
        print('Отбойный молоток')
    elif noise_level > 130:
        print('Громче некуда')


if __name__ == '__main__':
    inp_noise = int(input('Введите Ваш уровень шума: '))
    check_noise(inp_noise)
