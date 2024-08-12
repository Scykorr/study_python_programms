inp_string = (input().lower().replace('.', '').
              replace(',', '').replace(';', '').replace('-', '').
              replace(':', '').replace('?', '').replace('!', ''))
result = len(set(inp_string.split()))
print(result)
