inp_num_n = int(input())
inp_num_k = int(input())
result = 0
for i in range(1, inp_num_n + 1):
    result = (result + inp_num_k) % i
print(result + 1)
