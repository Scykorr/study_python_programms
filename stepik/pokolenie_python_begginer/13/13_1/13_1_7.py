# объявление функции
def draw_box():
    for index in range(14):
        if index == 0 or index == 13:
            print('*' * 10)
        else:
            print('*' + ' ' * 8 + '*')

# основная программа
draw_box()  # вызов функции