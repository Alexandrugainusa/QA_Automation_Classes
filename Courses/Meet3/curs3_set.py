"""
Curs 3 - Set
"""
from typing import Set, Union

my_set: set[Union[str, int, bool]] = {'John', 7, 5, True, 'case'}
my_set.add(17)
print(my_set)
# my_set.pop()
# my_set.pop()
# print(my_set)
my_list = [3, 2, 5, 1, 7, 3, 1]
print(list(set(my_list)))  # lista cu valori unice
second_set = {3, 5, 7, 8, 'case'}
print(second_set.difference(my_set)) # diferente
# print(second_set - my_set)
print(second_set.intersection(my_set))
# print(second_set & my_set)
