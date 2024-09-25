my_dict={"Илья": 1978,"Алина": 2001,"Пётр": 1999}
print(my_dict)
print(my_dict.get("Илья"))
print(my_dict.get("Люба"))
print(my_dict)
my_dict.update({"Эля": 1985,
                "Семён":1988})
print(my_dict)
del my_dict['Алина']
print(my_dict)

my_set={1,2,3,1,2,3,4,5,6,8}
print(my_set)
my_set.add(9)
print(my_set)
my_set.remove(5)
print(my_set)
