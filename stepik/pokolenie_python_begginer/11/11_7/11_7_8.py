inp_list = input().split()
inp_list = [int(el) ** 3 for el in inp_list]
for el in inp_list:
    print(el, end=' ')
