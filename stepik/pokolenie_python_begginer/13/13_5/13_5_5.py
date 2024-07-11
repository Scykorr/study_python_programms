# объявление функции
def is_password_good(password):
    flag = True
    if len(password) < 8 or len([el for el in password if el.isupper()]) == 0 or len(
            [el for el in password if el.islower()]) == 0 or len([el for el in password if el.isdigit()]) == 0:
        flag = False
    return flag

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
