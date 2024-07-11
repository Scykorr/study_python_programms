# объявление функции
def get_shipping_cost(quantity):
    result_sum = 1000 + (quantity - 1) * 120
    return result_sum


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
