# объявление функции
def number_of_factors(num):
    return len([el for el in range(1, num + 1) if num % el == 0])


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
