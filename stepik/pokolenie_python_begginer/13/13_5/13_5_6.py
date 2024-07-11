# объявление функции
def is_one_away(word1, word2):
    flag = False
    if len(word1) == len(word2):
        if len([el for index, el in enumerate(word1) if el != word2[index]]) == 1:
            flag = True
    return flag


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
