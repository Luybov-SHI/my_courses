grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students=sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
a={students[0]:sum(grades[0]) / len(grades[0],)}
b={students[1]:sum(grades[1]) / len(grades[1],)}
c={students[2]:sum(grades[2]) / len(grades[2],)}
d={students[3]:sum(grades[3]) / len(grades[3],)}
e={students[4]:sum(grades[4]) / len(grades[4],)}
print(a|b|c|d|e)





