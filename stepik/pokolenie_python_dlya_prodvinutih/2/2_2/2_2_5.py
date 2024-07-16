inp_num_list = list(map(int, input().split()))
total_counter = 1
first_number = inp_num_list[0]
for el in inp_num_list[1:]:
    if first_number != el:
        total_counter += 1
        first_number = el
print(total_counter)
