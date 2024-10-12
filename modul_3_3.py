def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c =[1, 2, 3])

print('_________________________________')

values_list = [10, 'текст', False]
values_dict = {'a': 20, 'b': 'знак', 'c': False}
print_params(*values_list)
print_params(**values_dict)

print('_________________________________')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)