inp_timur = input()
inp_ruslan = input()
play_list = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']
if play_list.index(inp_timur) == play_list.index(inp_ruslan):
    print('ничья')
elif (play_list.index(inp_timur) - play_list.index(inp_ruslan)) % 2 == 0:
    if play_list.index(inp_timur) > play_list.index(inp_ruslan):
        print('Тимур')
    else:
        print('Руслан')
elif (play_list.index(inp_timur) - play_list.index(inp_ruslan)) % 2 != 0:
    if play_list.index(inp_timur) > play_list.index(inp_ruslan):
        print('Руслан')
    else:
        print('Тимур')
