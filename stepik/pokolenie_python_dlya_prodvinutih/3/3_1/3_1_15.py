# объявление функции
def func(num1, num2):
    flag = False
    if num1 % num2 == 0:
        flag = True
    return flag


# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print('делится')
else:
    print('не делится')
