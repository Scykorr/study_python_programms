list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = 0
for el in list1:
    if maximum < max(el):
        maximum = max(el)
print(maximum)
