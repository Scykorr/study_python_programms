# объявление функции
def is_palindrome(text):
    test_text = text.lower().replace(' ', '').replace('!', '').replace(',', '').replace('.', '').replace('?',
                                                                                                         '').replace(
        '-', '')
    flag = False
    if test_text == test_text[::-1]:
        flag = True
    return flag


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

