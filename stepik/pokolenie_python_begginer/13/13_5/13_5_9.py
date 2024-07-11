# объявление функции
def is_correct_bracket(text):
    result_sum = 0
    flag = True
    for el in text:
        if el == ')':
            result_sum -= 1
        elif el == '(':
            result_sum += 1
        if result_sum < 0:
            flag = False
            break
    if result_sum > 0:
        flag = False
    return flag


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
