inp_first_str = set(input().split())
inp_second_str = set(input().split())
print(*sorted(list(map(int, sorted(inp_first_str.intersection(inp_second_str))))))
