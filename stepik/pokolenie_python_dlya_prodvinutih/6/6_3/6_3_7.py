numbers = ((10, 10, 10, 12), (30, 45, 56, 45),
           (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
total_list = list()

for tup in numbers:
    total_list.append(sum(tup) / len(tup))

print(total_list)
