inp_num = input()
new_num = ''
if len(inp_num) == 5:
    new_num = inp_num[::-1]
elif len(inp_num) == 6:
    new_num = inp_num[0] + inp_num[1:][::-1]
print(int(new_num))
