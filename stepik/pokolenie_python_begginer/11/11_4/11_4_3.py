num_amount = int(input())
first_list = list()
result_list = list()
for _ in range(num_amount):
    inp_num = int(input())
    first_list.append(inp_num)
    result_list.append((pow(inp_num, 2) + 2 * inp_num + 1))
print(*first_list, sep='\n')
print()
print(*result_list, sep='\n')
