from math import floor

inp_n = int(input())
name_set = set()
result_list = list()
for _ in range(inp_n):
    inp_result = input().split(': ')
    if inp_result[0] not in name_set:
        name_set.add(inp_result[0])
        result_list.append(inp_result)
    else:
        for el in result_list:
            if inp_result[0] in el:
                el.append(inp_result[1])

counter_true_answers = 0
counter_all_answers = 0
counter_correct_answers = 0
for el in result_list:
    counter_all_answers += (len(el) - 1)
    if 'Correct' in el:
        counter_true_answers += 1
        counter_correct_answers += el.count('Correct')
if counter_true_answers != 0:
    print(f'Верно решили {counter_true_answers} учащихся')
    print(f'Из всех попыток {floor(counter_correct_answers / counter_all_answers * 100 + 0.5)}% верных')
else:
    print('Вы можете стать первым, кто решит эту задачу')
