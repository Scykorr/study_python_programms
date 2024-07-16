inp_str = input()
max_counter = 0
curr_counter = 0
for el in inp_str:
    if el == 'Р':
        curr_counter += 1
    else:
        curr_counter = 0
    if curr_counter > max_counter:
        max_counter = curr_counter
print(max_counter)
