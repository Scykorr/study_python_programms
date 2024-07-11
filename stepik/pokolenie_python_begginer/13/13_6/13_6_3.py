# объявление функции
def get_middle_point(x1, y1, x2, y2):
    res_x = (x1 + x2) / 2
    res_y = (y1 + y2) / 2
    return res_x, res_y


# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
