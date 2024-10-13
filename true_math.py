from math import inf # Бесконечность можно импортировать из встроенной библиотеки math
def divide(first, second):
    if second == 0:
        return inf
    else:
        return first/second