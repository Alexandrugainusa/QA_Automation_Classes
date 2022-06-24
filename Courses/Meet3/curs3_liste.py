"""
Curs 3
"""
from typing import List, Union

basket: list[Union[str, int, bool]] = ['1', '12', 2022, 'name', True, 'a']
basket2 = ['1', '12', 2022, 'prename', False, 'c', [2, 3, 7, 5]]
print(basket[-1])
print(basket.count('a'))  # te ajuta sa identifici de cate ori se gaseste un element in lista ta
print(len(basket))
x = basket[::-1]
print(x)
# Todo - de repetat slicing pe lista
print(basket2[-1][2])

basket2[1] = 7
print(basket2)  # mutabilitate

basket3 = [basket, basket2]
print(basket3)

combined = basket + basket2
print(combined)

basket3.extend(basket)
print(basket3)

print(basket3[1][3])

my_matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
print(my_matrix[1][1])

# Todo - sa inversam liniile cu coloanele

print(basket3.append('x'))
print(basket3)

# Todo - ctrl + click -> ptr documentare (ex. append)

