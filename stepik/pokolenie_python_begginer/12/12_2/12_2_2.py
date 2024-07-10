first_inp_string = list(map(int, input().split()))
second_inp_string = list(map(int, input().split()))
print(*[first_inp_string[i] + second_inp_string[i] for i in range(len(first_inp_string))], sep=' ')
