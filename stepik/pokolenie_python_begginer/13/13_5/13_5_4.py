# объявление функций
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


def get_next_prime(num):
    num += 1
    while not (is_prime(num)):
        num += 1
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
