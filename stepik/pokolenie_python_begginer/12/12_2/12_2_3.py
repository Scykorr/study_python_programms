inp_num_list = list(map(int, input().split()))
print(*inp_num_list, sep='+', end='')
print(f'={sum(inp_num_list)}')
