# объявление функции
def get_month(language, number):
    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
          'декабрь']
    en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
          'november', 'december']
    result = ''
    if language == 'ru':
        result = ru[number]
    elif language == 'en':
        result = en[number]
    return result


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
