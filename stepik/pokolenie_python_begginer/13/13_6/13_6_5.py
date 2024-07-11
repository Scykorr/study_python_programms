from math import sqrt


# объявление функции
def solve(inp_a, inp_b, inp_c):
    discriminant = pow(inp_b, 2) - 4 * inp_a * inp_c
    if (inp_a != 0) and (discriminant >= 0):
        if discriminant > 0:
            first_root = (- inp_b - sqrt(pow(inp_b, 2) - 4 * inp_a * inp_c)) / (2 * inp_a)
            second_root = (- inp_b + sqrt(pow(inp_b, 2) - 4 * inp_a * inp_c)) / (2 * inp_a)
            return min(first_root, second_root), max(first_root, second_root)
        else:
            root = - inp_b / (2 * inp_a)
            return root, root


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
