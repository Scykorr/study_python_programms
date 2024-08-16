first_num = set(input())
second_num = set(input())
if first_num.isdisjoint(second_num):
    print('NO')
else:
    print('YES')
