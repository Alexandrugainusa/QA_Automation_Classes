"""
Curs 7.1 Exceptions.
"""
# cod functional
try:
    lista = [3, 4, 5]
    print(lista[12])
except IndexError as e:
    print(e)
finally:
    print('Orice ar fi ajung aici')

# cod cu eroare
# lista = [3, 4, 5]
# print(lista[12])
