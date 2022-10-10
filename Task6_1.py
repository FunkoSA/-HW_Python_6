
spisok = ['gfh', 'gfh2', '67', '32j23', '32put2']
num_spisok = list(enumerate((spisok),1))
number =32
result = list(filter(lambda s: str(number) in s[1] , num_spisok))
if len(result) > 0:
    print (f'Элемент {number} в списке {spisok}\nНаходится на позициях:{result}')
else:
    print (f'Элемент {number} в списке {spisok} не найден')
