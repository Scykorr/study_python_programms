# объявление функции
def is_valid_triangle(side1, side2, side3):
    flag = True
    if ((side1 + side2) > side3) and ((side1 + side3) > side2) and (
            (side2 + side3) > side1):
        pass
    else:
        flag = False
    return flag


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
