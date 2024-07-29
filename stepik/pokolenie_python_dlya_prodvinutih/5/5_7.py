x, y = input()
n = 8
matrix = [['.'] * n for _ in range(n)]
y = n - int(y)
x = ord(x) - 97
for i in range(n):
    for q in range(n):
        if i == y or q == x:
            matrix[i][q] = '*'
        elif (i + q == y + x) or (i - q == y - x):
            matrix[i][q] = '*'

matrix[y][x] = 'Q'

for x in range(n):
    print(*matrix[x])
