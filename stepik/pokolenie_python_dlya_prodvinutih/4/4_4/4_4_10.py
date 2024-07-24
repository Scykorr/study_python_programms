inp_num = int(input())
matrix = [list(map(int, input().split())) for _ in range(inp_num)]
total_sum = 0
for i in range(inp_num):
    for j in range(inp_num):
        if i == j:
            total_sum += matrix[i][j]
print(total_sum)
