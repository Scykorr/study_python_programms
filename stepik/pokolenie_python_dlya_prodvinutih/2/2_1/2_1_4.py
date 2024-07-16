len_inp_string = len(input())
total_price = 60 * len_inp_string
rubles = total_price // 100
kopecks = total_price % 100
print('{total_rubles} р. {total_kopecks} коп.'.format(
    total_rubles=rubles,
    total_kopecks=kopecks))
