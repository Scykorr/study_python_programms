inp_word = input()
total_string = inp_word + ' запретил букву'
total_list = list(total_string)
check_list = total_list.copy()
check_list = list(set(check_list))
check_list.remove(' ')
check_list.sort()
for el in check_list:
    print(*total_list, el)
    for el_2 in total_list:
        if el_2 == el:
            total_list.remove(el)
