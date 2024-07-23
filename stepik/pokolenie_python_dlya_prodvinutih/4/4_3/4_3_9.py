input_num = int(input())
print(*[[el for el in range(1, curr_num + 1)] for curr_num in range(1, input_num + 1)], sep='\n')
