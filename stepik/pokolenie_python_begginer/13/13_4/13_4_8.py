# объявление функции
def get_factors(num):
    return [el for el in range(1, num + 1) if num % el == 0]


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
