def draw_triangle(fill, base):
    for i in range(base // 2):
        print(fill * (i + 1))
    for i in range(base // 2, -1, -1):
        print(fill * (i + 1))
fill = input()       # Запрос символа для заполнения треугольника
base = int(input())  # Запрос размера основания треугольника
draw_triangle(fill, base)