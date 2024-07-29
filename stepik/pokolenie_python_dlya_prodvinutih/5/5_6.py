import numpy as np

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = np.array(matrix)
result = 'YES'
for i in range(n):
    for count in range(1, n + 1):
        if count not in m[:, i]:
            result = 'NO'
        if count not in m[i]:
            result = 'NO'
print(result)
