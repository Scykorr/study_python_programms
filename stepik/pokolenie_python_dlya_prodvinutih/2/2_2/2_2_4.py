inp_num_list = list(map(int, input().split()))
inp_num_list.insert(0, inp_num_list.pop(-1))
print(*inp_num_list)
