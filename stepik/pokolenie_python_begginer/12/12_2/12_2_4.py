inp_number = input().split('-')
flag = False
if (len(inp_number) == 4 and inp_number[0] == '7') or len(inp_number) == 3:
    if len(inp_number[-1]) == 4 and inp_number[-1].isdigit() and len(inp_number[-2]) == 3 and inp_number[
        -2].isdigit() and len(inp_number[-3]) == 3 and inp_number[-3].isdigit():
        flag = True

if flag:
    print('YES')
else:
    print('NO')
