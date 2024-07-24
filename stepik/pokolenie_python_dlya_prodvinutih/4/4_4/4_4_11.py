inp_num = int(input())
matrix = [list(map(int, input().split())) for _ in range(inp_num)]
for el in matrix:
    counter = 0
    for num in el:
        if num > (sum(el) / len(el)):
            counter += 1
    print(counter)
