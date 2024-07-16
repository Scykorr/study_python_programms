inp_num_list = list(map(int, input().split()))
if len(inp_num_list) % 2 == 0:
    step = 1
else:
    step = 2
for index in range(0, len(inp_num_list) - step, 2):
    inp_num_list[index], inp_num_list[index + 1] = inp_num_list[index + 1], inp_num_list[index]
print(*inp_num_list)
