inp_year = int(input())
animals_list = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр',
                'Заяц']
print(animals_list[inp_year % 12 - 8])
