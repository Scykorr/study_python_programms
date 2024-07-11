# объявление функции
def find_all(target, symbol):
    return [index for index, el in enumerate(target) if el == symbol]


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
