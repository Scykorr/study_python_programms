# объявление функции
def print_digit_sum(num):
    result_sum = 0
    for el in str(num):
        result_sum += int(el)
    print(result_sum)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
