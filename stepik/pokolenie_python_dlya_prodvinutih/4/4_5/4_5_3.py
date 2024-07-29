inp_row = int(input())
inp_column = int(input())
matrix = [list(map(int, input().split())) for _ in range(inp_row)]
inp_column_i, inp_column_j = map(int, input().split())
for row in matrix:
    row[inp_column_i], row[inp_column_j] = row[inp_column_j], row[inp_column_i]
for row in matrix:
    print(*row)
