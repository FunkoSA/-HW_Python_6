import math
spisok = [2, 3, 4, 5, 6] 
result_spisol =list(map(lambda x, y: x * y, spisok[:math.ceil(len(spisok)/2)], spisok[:-(math.ceil(len(spisok)/2)+1):-1]))
print(f'Резельтат перемножения пары элементов (первый-последний, второй-предпоследний и тд) для списка:\n{spisok}\nСледующий:\n{result_spisol}')

