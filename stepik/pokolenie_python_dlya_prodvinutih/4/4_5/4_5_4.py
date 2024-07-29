inp_n = int(input())
matrix = [list(map(int, input().split())) for _ in range(inp_n)]
flag = 'YES'
for i in range(inp_n):
    for j in range(inp_n):
        if i == j:
            continue
        elif matrix[i][j] == matrix[j][i]:
            continue
        else:
            flag = 'NO'
            break
    if flag == 'NO':
        break
print(flag)
