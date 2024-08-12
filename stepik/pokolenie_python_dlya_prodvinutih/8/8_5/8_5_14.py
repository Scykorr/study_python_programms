inp_list = list(map(int, input().split()))
test_set = set()
for el in inp_list:
    if el in test_set:
        print('YES')
    else:
        test_set.add(el)
        print('NO')
