"""
For.
"""

lst = ['mama', 'tata', 'mama', 'bunicu', 'masina', 'name', 'roata', 'masina']
# print(list(set(lst)))
lst2 = []
# ToDo - DUPLICATE
# for i in range(0, len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]: # se compara indexul
#             lst2.append(lst[i])
# print(lst2)

# ToDo - use count - (sa rezolvam printr-un singur for)

# ToDo - SORTARE
lst3 = [1, 4, 3, 2, 5, 100, 87, 101, 45, 50, 1, 4, 5, 3, 5, 7, 4]
# ToDo - BUBBLE SORT
for i in range(0, len(lst3)):  # cate elemente -> atatea comparatii
    for j in range(0, len(lst3)-1):
        if lst3[j] > lst3[j + 1]:
            aux = lst3[j]
            lst3[j] = lst3[j + 1]
            lst3[j + 1] = aux
print(lst3)

#ToDo - SELECTION SORT
