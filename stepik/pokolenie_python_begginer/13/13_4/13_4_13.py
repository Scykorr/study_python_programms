# объявление функции
def merge() -> list:
    inp_amount = int(input())
    result_merge = []
    for i in range(inp_amount):
        result_merge = sorted(result_merge + [int(c) for c in input().split()])
    return result_merge


# вызываем функцию
print(*merge())
