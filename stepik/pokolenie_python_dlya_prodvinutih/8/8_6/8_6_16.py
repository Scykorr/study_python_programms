inp_n = int(input())
first_set = set([el for el in input()])
for _ in range(inp_n - 1):
    first_set = first_set.intersection(set([el for el in input()]))

if first_set:
    print(*sorted(first_set))
