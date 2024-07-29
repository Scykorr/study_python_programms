inp_n = int(input())
inp_m = int(input())
mult = [[0] * inp_m for _ in range(inp_n)]
for i in range(inp_n):
    for j in range(inp_m):
        mult[i][j] = i * j
for row in mult:
    for el in row:
        print(str(el).ljust(3), end='')
    print()
