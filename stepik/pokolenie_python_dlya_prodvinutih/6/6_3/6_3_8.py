inp_a = int(input())
inp_b = int(input())
inp_c = int(input())

coord_x = -inp_b / (2 * inp_a)
coord_y = (4 * inp_a * inp_c - pow(inp_b, 2)) / (4 * inp_a)
print((coord_x, coord_y))
