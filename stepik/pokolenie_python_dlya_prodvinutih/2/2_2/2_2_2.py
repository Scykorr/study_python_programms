inp_num_list = list(map(int, input().split()))
total_counter = 0
for index in range(len(inp_num_list) - 1):
    if inp_num_list[index] < inp_num_list[index + 1]:
        total_counter += 1
print(total_counter)
