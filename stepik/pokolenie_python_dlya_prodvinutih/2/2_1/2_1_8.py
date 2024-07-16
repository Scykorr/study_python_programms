inp_num = input()
new_num = list(inp_num[::-1])
counter_el = 0
for el in range(3, len(new_num), 3):
    new_num.insert(el + counter_el, ',')
    counter_el += 1
print(*(new_num[::-1]), sep='')
