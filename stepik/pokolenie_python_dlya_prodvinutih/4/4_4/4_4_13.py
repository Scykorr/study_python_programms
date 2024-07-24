n = int(input())
s = []

for i in range(n):
    f = [int(i) for i in input().split()]
    for j in range(len(f)):
        if (j <= i <= n - 1 - j) or (j >= i >= n - 1 - j) or (i == j) or (i + j + 1 == n):
            s.append(f[j])

print(max(s))
