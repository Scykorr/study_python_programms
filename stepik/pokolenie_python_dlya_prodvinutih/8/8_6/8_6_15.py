inp_first_str = set(input().split())
inp_second_str = set(input().split())
print(*sorted(list(map(int, sorted(inp_first_str - inp_second_str)))))
