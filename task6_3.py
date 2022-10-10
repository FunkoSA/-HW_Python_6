
import math
a = '12 3 3'
array_a = list(map(int,a.split(' ')))
b = '2 64 66'
array_b = list(map(int,b.split(' ')))
distance = round(math.sqrt(sum(list(map(lambda a, b:(b - a) ** 2, array_b, array_a)))),2)
print (distance)

