inp_n = int(input())
student_list = [tuple(input().split()) for _ in range(inp_n)]
good_marks = [el for el in student_list if int(el[1]) >= 4]
for el in student_list:
    print(*el)
print()
for el in good_marks:
    print(*el)
