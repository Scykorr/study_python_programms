inp_n = int(input())
matrix = [list(map(int, input().split())) for _ in range(inp_n)]
counter = 0
for column_index in range(inp_n):
    matrix[column_index][counter], matrix[-1 - counter][column_index] = matrix[-1 - counter][column_index], \
        matrix[column_index][counter]
    counter += 1
for row in matrix:
    print(*row)
