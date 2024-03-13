a = int(input('Введите число a: ')) 

if a > 0 and a < 6:
    print('Близкие ')
elif a > 5 and a < 26: 
    print('Далёкие')
elif a > 25:
    print('Сверхдалёкие ')
else:
    print('ошибка данных')
 
