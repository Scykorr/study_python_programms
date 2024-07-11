# объявление функции
def convert_to_python_case(text):
    new_str = ''
    for index, el in enumerate(text):
        if index == 0:
            new_str += el.lower()
        elif index != 0 and el.isupper():
            new_str += f'_{el.lower()}'
        else:
            new_str += el
    return new_str


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
