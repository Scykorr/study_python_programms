"""Упражнение 33. Сортировка трех чисел"""


def get_filter_list(inp_list: list) -> None:
    max_val = max(inp_list)
    min_val = min(inp_list)
    middle_num = sum(inp_list) - max_val - min_val
    print(f'Отсортированный список: {min_val}, {middle_num}, {max_val}')


if __name__ == '__main__':
    nums_list = []
    for el in range(1, 4):
        nums_list.append(int(input(f'Введите число №{el}: ')))
    get_filter_list(inp_list=nums_list)
