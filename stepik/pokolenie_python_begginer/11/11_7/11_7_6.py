palindromes = [x for x in range(100, 1001) if str(x) == str(x)[::-1]]
print(palindromes)
