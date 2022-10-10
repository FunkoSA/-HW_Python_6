from sre_compile import isstring


def str_find (array, str_f, enter_number):
    array = list(enumerate((array),1))
    filtered_str = list(filter(lambda s:  str_f in s[1] if isstring(s[1])  else ''  , array))
    if len(filtered_str) < enter_number:
        return 'ответ: -1'
    else:
        return filtered_str[enter_number-1][0]

spisok1 = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
find = "qwe"
n = 2
result = str_find(spisok1, find, n)
print (f'Для списка:{spisok1} вхождение №{n} искомого "{find}" следующее:\n{result}')

spisok1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] #, ищем: "йцу", ответ: 5
find = "йцу"
n = 3
result = str_find(spisok1, find, n)
print (f'Для списка:{spisok1} вхождение №{n} искомого "{find}" следующее:\n{result}')
spisok1 = ["йцу", "фыв", "ячс", "цук", "йцукен"] #, ищем: "йцу", ответ: -1
find = "йцу"
n = 2
result = str_find(spisok1, find, n)
print (f'Для списка:{spisok1} вхождение №{n} искомого "{find}" следующее:\n{result}')

spisok1 = ["123", "234", 123, "567"] #, ищем: "123", ответ: -1
find = "123"
n = 2
result = str_find(spisok1, find, n)
print (f'Для списка:{spisok1} вхождение №{n} искомого {find} следующее:\n{result}')

spisok1 = [] #, ищем: "123", ответ: -1
find = "123"
n = 2
result = str_find(spisok1, find, n)
print (f'Для списка:{spisok1} вхождение №{n} искомого {find} следующее:\n{result}')

