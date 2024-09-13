"Упражнение 37. Гласные и согласные"


def check_letter(letter) -> None:
    letter = letter.lower()
    list_of_gl = ['a', 'e', 'i', 'o', 'u']
    if letter in list_of_gl:
        print('Буква гласная')
    elif letter == 'y':
        print('Буква может быть как гласной так и согласной')
    else:
        print('Буква согласная')


if __name__ == '__main__':
    inp_letter = input('Введите букву латинского алфавита: ')
    check_letter(inp_letter)
