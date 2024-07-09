inp_string_amount = int(input().split('#')[1])
result_list = list()
for _ in range(inp_string_amount):
    inp_string = input()
    result_list.append(inp_string.split('#'))
    if '#' in inp_string:
        del result_list[-1][-1]
for index, el in enumerate(result_list):
    result_list[index][0] = el[0].rstrip()
    print(*el)
