n = int(input('Введите последовательность чисел: '))
count = 1
m = n
while n != 0:
    n = int(input('Введите следующее число: '))
    count += 1
    m += n
print('Вы ввели ' + str(count)+ ' чисел')


