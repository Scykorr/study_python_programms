inp_n = int(input())
matrix = [list(map(int, input().split())) for _ in range(inp_n)]
for index in range(-1, -inp_n - 1, -1):
    print(*matrix[index])
