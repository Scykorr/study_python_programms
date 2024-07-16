inp_num_amount = int(input())
num_list = list()
for _ in range(inp_num_amount):
    num_list.append(int(input()))
main_num = int(input())
flag = 'НЕТ'
if len(num_list) == 1 and num_list[0] == main_num:
    flag = 'ДА'
elif len(num_list) > 1:
    for index, first_num in enumerate(num_list):
        for second_num in num_list[index+1:]:
            if first_num * second_num == main_num:
                flag = 'ДА'
                break
print(flag)
