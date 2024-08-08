tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'),
          (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [el for el in tuples if el]

print(non_empty_tuples)
