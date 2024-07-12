from random import choices

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
unidentified_letters = 'il1Lo0O'


def generate_password(length, chars_list):
    password = choices(chars_list, k=length)
    return password


password_amount = int(input('Сколько паролей генерировать?: '))
password_length = int(input('Введите длину пароля: '))
cipher_include = input('Включать ли цыфры? да/нет: ')
upper_letter_include = input('Включать ли прописные буквы? да/нет: ')
lower_letter_include = input('Включать ли строчные буквы? да/нет: ')
symbols_include = input('Включать ли символы "!#$%&*+-=?@^_"? да/нет: ')
unidentified_letters_include = input('Исключать ли неоднозначные символы "il1Lo0O"? да/нет: ')
chars = ''
if cipher_include == 'да':
    chars += digits
if upper_letter_include == 'да':
    chars += uppercase_letters
if lower_letter_include == 'да':
    chars += lowercase_letters
if symbols_include == 'да':
    chars += punctuation
if unidentified_letters_include == 'да':
    chars += unidentified_letters
for _ in range(password_amount):
    print(*generate_password(password_length, chars), sep='')

