inp_row = int(input())
inp_column = int(input())
matrix = [[''] * inp_column for _ in range(inp_row)]
for i in range(inp_row):
    for j in range(inp_column):
        matrix[i][j] = input()

for el in matrix:
    print(*el)
