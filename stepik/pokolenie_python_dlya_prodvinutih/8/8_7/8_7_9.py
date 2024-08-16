first_num = set(input())
second_num = set(input())
if first_num.issuperset(second_num):
    print('YES')
else:
    print('NO')
