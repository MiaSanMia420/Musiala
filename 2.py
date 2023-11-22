result = [index for index, (elem_v1, elem_v2) in enumerate(zip(v1, v2)) if elem_v1 % 2 == 0 and elem_v2 % 2 != 0]
print(result)
