first_mark_set = set(map(int, (input().split())))
second_mark_set = set(map(int, (input().split())))
third_mark_set = set(map(int, (input().split())))
print(*sorted(first_mark_set.intersection(second_mark_set) - third_mark_set, reverse=True))
