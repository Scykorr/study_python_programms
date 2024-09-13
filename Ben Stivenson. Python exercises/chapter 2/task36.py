"Упражнение 36. Собачий возраст"


def count_dog_age(people_age) -> str:
    dog_age = 0
    if people_age < 0:
        return "Вы ввели отрицательное число"
    for age in range(1, people_age + 1):
        if age <= 2:
            dog_age += 10.5
        else:
            dog_age += 4
    return dog_age


if __name__ == '__main__':
    inp_people_age = int(input('Ввведите возраст человека для перевода в возраст собаки: '))
    res_dog_age = count_dog_age(inp_people_age)
    print('Возраст собаки в расчете на человеческие года:', res_dog_age)
