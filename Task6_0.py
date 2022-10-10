""" 
import re
from collections import namedtuple
 
Token = namedtuple('Token', ['type', 'value'])
 
# Определяем шаблоны
# NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' # шаблон для выражений типа 'foo = 1 + 1'
# EQ = r'(?P<EQ>=)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
MULTIPLY = r'(?P<MULTIPLY>\*)'
DEVIDE = r'(?P<DEVIDE>\/)'
WS = r'(?P<WS>\s+)'
 
 
def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
 
master_pat = re.compile('|'.join([NUM, PLUS, MINUS, MULTIPLY, DEVIDE, WS]))
 
for tok in generate_tokens(master_pat, '42+7-12'):
    print(tok)
 """
""" 
 Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,. приоритет операций стандартный.
Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
*Пример:
2+2 => 4;
1+2*3 => 7;

10/2*5 => 25;
10 * 5 * => недостаточно числовых данных
-5 + 5 => 0
два + три => неправильный ввод: нужны числа
(2+((5-3)*(16-14)))/3 => 2
(256 - 194 => некорректная запись скобок
"""

string_for_scale='10-6/2*5+20-8/4+2*3'
print('Строка для вычисления: ', string_for_scale)
operators = {
            '*': lambda x,y : x*y,
            '/': lambda x,y : x/y,
            '+': lambda x,y : x+y,
            '-': lambda x,y : x-y,
            }

def get_numbers (expression):
    numbers =[]
    temp_value =''
    for i in expression:
        if i.isdigit():
            temp_value+=i
        elif len(temp_value)>0:
            numbers.append(temp_value)
            numbers.append(i)
            temp_value=''
        else:
            numbers.append(i)
    numbers.append(temp_value)
    numbers = list(filter(lambda char: char.isdigit(), numbers))
    return numbers

def get_operators (expression):
    return list(filter(lambda char: char in '+-/*', expression))

def get_parentheses(expression):
    return list(filter(lambda char: char in '()', expression))

def check_alpha (expression):
    return not any(filter(lambda char: char.isalpha(), expression))

def check_expression (numbers , opers):
    return True if len(numbers) > len(opers) else False

if check_alpha(string_for_scale):
    numbres_list = get_numbers(string_for_scale)
    operators_list = get_operators (string_for_scale)
    if check_expression (numbres_list, operators_list):
        print ('Список операндов и операторов: ', numbres_list, operators_list)
    else:
        print ('Выражение не полное ', numbres_list, operators_list)
else:
    print ('В исходном выраэении присутствуют буквы')

while len(operators_list) >0:
    while any(filter(lambda oper: oper in '/*', operators_list)):
        if any(filter(lambda oper: oper in '/', operators_list)) and any(filter(lambda oper: oper in '*', operators_list)):
            operator_index=min(operators_list.index('*'),operators_list.index('/'))
            operaition_result=operators.get(operators_list[operator_index])(int(numbres_list[operator_index]),int(numbres_list[operator_index+1]))
            del operators_list[operator_index]
            del numbres_list[operator_index]
            numbres_list[operator_index]=operaition_result
        elif any(filter(lambda oper: oper in '/', operators_list)):
            operator_index=operators_list.index('/')
            operaition_result=operators.get(operators_list[operator_index])(int(numbres_list[operator_index]),int(numbres_list[operator_index+1]))
            del operators_list[operator_index]
            del numbres_list[operator_index]
            numbres_list[operator_index]=operaition_result
        else:
            operator_index=operators_list.index('*')
            operaition_result=operators.get(operators_list[operator_index])(int(numbres_list[operator_index]),int(numbres_list[operator_index+1]))
            del operators_list[operator_index]
            del numbres_list[operator_index]
            numbres_list[operator_index]=operaition_result
    
    operaition_result=operators.get(operators_list[0])(int(numbres_list[0]),int(numbres_list[1]))
    del operators_list[0]
    del numbres_list[0]
    numbres_list[0]=operaition_result


print (f'Результат вычисления {string_for_scale} = {numbres_list[0]}')



