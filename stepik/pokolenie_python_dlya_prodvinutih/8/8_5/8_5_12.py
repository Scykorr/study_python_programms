inp_n = int(input())
res_string = ''
for _ in range(inp_n):
    res_string += input().lower()
print(len(set(res_string)))
