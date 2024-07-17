inp_word = input()
total_string = inp_word + ' запретил букву'
total_list = list(total_string)
check_list = total_list.copy()
check_list = list(set(check_list))
check_list.remove(' ')
check_list.sort()
for el in check_list:
    new_str = ''.join(total_list).split()
    print(*new_str, end=' ')
    print(el)
    for _ in range(total_list.count(el)):
        total_list.remove(el)
