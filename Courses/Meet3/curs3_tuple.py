"""
Curs3 - Tuple
"""

my_tuple = (3, 5, 7, 8, 1, 'something')
print(my_tuple[0])  # printeaza primul index

# my_tuple[0] = 5  imutable

second_tuple = 3, 5, 8, 1, 'home', True
print(type(second_tuple))

# Todo - try list methods for tuple

print(my_tuple.count(7)) # de cate ori apare 7
print(my_tuple.index(1)) # indexul lui 1

for x in my_tuple:
    print(x)