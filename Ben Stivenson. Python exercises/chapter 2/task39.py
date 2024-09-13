"Упражнение 39. Сколько дней в месяце?"


def check_month(month_name):
    if month_name == 'Январь':
        print(31)
    elif month_name == "Февраль":
        print("28 или 29, в зависимости от високосности года")
    elif month_name == "Март":
        print(31)
    elif month_name == "Апрель":
        print(30)
    elif month_name == "Май":
        print(31)
    elif month_name == "Июнь":
        print(30)
    elif month_name == "Июль":
        print(31)
    elif month_name == "Август":
        print(31)
    elif month_name == "Сентябрь":
        print(30)
    elif month_name == "Октябрь":
        print(31)
    elif month_name == "Ноябрь":
        print(30)
    elif month_name == "Декабрь":
        print(31)


if __name__ == '__main__':
    inp_month_name = input("Введите название месяца: ")
    check_month(inp_month_name)
