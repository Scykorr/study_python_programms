inp_num_amount = int(input())
total_list = list()
counter_num = 1
for _ in range(inp_num_amount):
    test_list = ['a', 'n', 't', 'o', 'n']
    inp_str = input()
    for el in inp_str:
        if len(test_list) == 0:
            break
        if test_list[0] == el:
            test_list.pop(0)
    if len(test_list) == 0:
        total_list.append(counter_num)
    counter_num += 1
print(*total_list)
