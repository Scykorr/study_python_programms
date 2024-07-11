# объявление функции
def is_pangram(text):
    alphabyte = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    counter = 0
    for el in alphabyte:
        if el in text.lower():
            counter += 1
    if counter == 26:
        return True
    else:
        return False

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
