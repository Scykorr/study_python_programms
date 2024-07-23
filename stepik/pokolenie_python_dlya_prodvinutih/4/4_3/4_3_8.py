input_num = int(input())
print(*[[el for el in range(1, input_num + 1)] for _ in range(input_num)], sep='\n')
