inp_num = int(input())
result_list = [el ** 2 for el in range(1, inp_num + 1)]
print(*result_list, sep='\n')
