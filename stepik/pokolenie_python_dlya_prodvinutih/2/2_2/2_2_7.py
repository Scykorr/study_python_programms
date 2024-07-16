inp_timur = input()
inp_ruslan = input()
if (inp_timur == 'камень' and inp_ruslan == 'ножницы' or inp_timur == 'бумага' and inp_ruslan == 'камень' or
        inp_timur == 'ножницы' and inp_ruslan == 'бумага'):
    print('Тимур')
elif (inp_timur == 'ножницы' and inp_ruslan == 'камень' or inp_timur == 'камень' and inp_ruslan == 'бумага' or
        inp_timur == 'бумага' and inp_ruslan == 'ножницы'):
    print('Руслан')
else:
    print('ничья')
