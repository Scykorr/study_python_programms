list_1, n, list_2, c = input().split(), int(input()), [], 0

for i in list_1:

    list_2 += [list_1[c::n]]

    c += 1

    if c == n:
        break

print(list_2)
