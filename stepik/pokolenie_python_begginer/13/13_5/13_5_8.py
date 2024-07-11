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


# объявление функции
def is_valid_password(password):
    numbers_list = password.split(':')
    flag = False
    if numbers_list[0] == numbers_list[0][::-1] and is_prime(int(numbers_list[1])) and int(
            numbers_list[2]) % 2 == 0 and len(numbers_list) == 3:
        flag = True
    return flag


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
