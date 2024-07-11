# объявление функции
def get_days(month):
    result = 0
    if month == 2:
        result = 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        result = 31
    elif month in [4, 6, 9, 11]:
        result = 30
    return result


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
