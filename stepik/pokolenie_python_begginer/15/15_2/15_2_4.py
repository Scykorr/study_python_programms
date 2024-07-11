from math import log2, ceil

inp_num = int(input())
if inp_num == 1:
    print(1)
else:
    print(ceil(log2(inp_num + 1)))
