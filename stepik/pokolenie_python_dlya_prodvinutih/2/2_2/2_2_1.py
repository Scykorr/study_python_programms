inp_num_amount = int(input())
counter_first = 0
counter_second = 0
counter_third = 0
counter_fourth = 0
for _ in range(inp_num_amount):
    x_point, y_point = map(int, input().split())
    if x_point > 0 and y_point > 0:
        counter_first += 1
    elif x_point < 0 < y_point:
        counter_second += 1
    elif x_point < 0 and y_point < 0:
        counter_third += 1
    elif x_point > 0 > y_point:
        counter_fourth += 1
print('Первая четверть:', counter_first)
print('Вторая четверть:', counter_second)
print('Третья четверть:', counter_third)
print('Четвертая четверть:', counter_fourth)
