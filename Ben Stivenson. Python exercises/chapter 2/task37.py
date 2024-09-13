"Упражнение 37. Гласные и согласные"


def check_letter(letter):
    letter = letter.lower()
    list_of_gl = ['a', 'e', 'i', 'o', 'u']
    if letter in list_of_gl:
        print('Буква гласная')
    elif letter == 'y':
        print('Буква может быть как гласной так и согласной')
    else:
        print('Буква согласная')


if __name__ == '__main__':
    check_letter('a')
