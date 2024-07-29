n = int(input())
result = []
for i in range(n):
    result += (list(map(int, input().split())))[n - i - 1:]
print(max(result))
