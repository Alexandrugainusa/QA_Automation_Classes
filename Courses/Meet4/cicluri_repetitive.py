"""
Curs 4 - Cicluri Repetitive
"""

lst = [1, 3, 4, 6, 7, 8, 10, 11, 13, 17, 12, 24]
suma = 0  # contorizator
# for element in lst:
#     suma += element
#     print(suma)
# print(f'Suma elementelor este {suma}')

# x = len(lst)
# i = 0
# while i < x:
#     suma += lst[i]
#     i +=1
# print(suma)

# ToDo - cel mai mare numar par din lista
# c = 0
# for element in lst:
#     if element % 2 == 0 and element > c:
#         c = element
# print(c)

# ToDo folosind functia sort sa gasim cel mai mare numar par

from random import randint

x = randint(1, 10)
condition = True
while condition:  # atata timp cat conditia este valida se executa codul (condition == True)
    z = int(input('enter: '))
    if x == z:
        print('Lucky you')
        break
    else:
        print('more')

# ToDo - sa ne asiguram ca se introduce un int si ca userul nu introduce un String
