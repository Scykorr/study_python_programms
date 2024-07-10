print(*[int(el) ** 2 for el in input().split() if str(int(el) ** 2)[-1] != '4' and int(el) % 2 == 0], sep=' ')
