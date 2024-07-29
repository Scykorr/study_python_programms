inp_n = int(input())
inp_m = int(input())
matrix = []
for _ in range(inp_n):
    matrix.append(list(map(int, input().split())))
max_val = matrix[0][0]
max_r = 0
max_c = 0

for i_r, row in enumerate(matrix):
    for i_c, el in enumerate(row):
        if el > max_val:
            max_val = el
            max_r = i_r
            max_c = i_c
print(max_r, max_c)
