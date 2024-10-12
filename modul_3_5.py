def get_multiplied_digits(number):
    str_number = str(number)
    str_number = str(str_number.replace('0', ''))
    if len(str_number) > 1:
        first = int(str_number[0])
        if first !=0:
         return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)

result = get_multiplied_digits(40203)
print(result)