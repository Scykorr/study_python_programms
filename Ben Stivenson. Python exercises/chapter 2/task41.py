"""Упражнение 41. Классификация треугольников"""


def input_values():
    side_a = int(input('Введите первую сторону треугольника: '))
    side_b = int(input('Введите вторую сторону треугольника: '))
    side_c = int(input('Введите третью сторону треугольника: '))
    return side_a, side_b, side_c

def main():
    first_side, second_side, third_side = input_values()
    if first_side == second_side == third_side:
        print('Треугольник равносторонний.')
    elif first_side != second_side and second_side != third_side and first_side != third_side:
        print('Треугольник разносторонный')
    else:
        print('Треугольник равнобедренный.')

if __name__ == '__main__':
    main()