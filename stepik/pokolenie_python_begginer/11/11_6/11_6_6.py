inp_numbers = input().split()
inp_numbers = list(map(int, inp_numbers))
max_num = max(inp_numbers)
min_num = min(inp_numbers)
max_index = inp_numbers.index(max_num)
min_index = inp_numbers.index(min_num)
inp_numbers[max_index] = min_num
inp_numbers[min_index] = max_num
print(*inp_numbers)
