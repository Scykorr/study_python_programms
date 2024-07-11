# объявление функции
def is_prime(num):
    counter = 2
    flag = True
    if num == 0 or num == 1:
        flag = False
    for el in range(2, num):
        if num % el == 0:
            counter += 1
        if counter > 2:
            flag = False
    return flag


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
