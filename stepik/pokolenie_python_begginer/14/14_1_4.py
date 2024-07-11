# объявление функции
def draw_triangle():
    for el in range(1, 9):
        print(' ' * (8 - el) + '*' * (el * 2 - 1))


# основная программа
draw_triangle()  # вызов функции
