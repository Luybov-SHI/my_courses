first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first==second==third:
    print('3')
elif first==second or third==first or second:
    print('2')
elif first !=second !=third !=first:
    print('0')




