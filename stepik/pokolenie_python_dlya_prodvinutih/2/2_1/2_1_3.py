inp_weight = float(input())
inp_height = float(input())
result_imt = inp_weight / pow(inp_height, 2)
if result_imt > 25:
    print('Избыточная масса')
elif result_imt < 18.5:
    print('Недостаточная масса')
else:
    print('Оптимальная масса')
