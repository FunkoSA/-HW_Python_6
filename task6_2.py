
spisok = [2, 3, 4, 5, 6, 3, 4] 

sum_elements = sum(filter(lambda x: (spisok.index(x))%2,spisok))
print(sum_elements)