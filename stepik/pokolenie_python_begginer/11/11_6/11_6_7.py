inp_string_list = input().lower().split()
sum_article_a = inp_string_list.count('a')
sum_article_an = inp_string_list.count('an')
sum_article_the = inp_string_list.count('the')
result_sum = sum_article_a + sum_article_an + sum_article_the
print(f'Общее количество артиклей: {result_sum}')
