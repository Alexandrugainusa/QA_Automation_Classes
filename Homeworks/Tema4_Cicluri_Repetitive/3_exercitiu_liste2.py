"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for numar in numere:
    if numar == 3:  # cand vede valoarea 3
        count += 1
print(f"Am gasit numarul 3 de {count} ori in lista.")

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma = suma + numar
print(f'Suma numerelor din lista este {suma}')

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = numere[0]
for numar in numere:
    if numar > maxim:
        maxim = numar
print(f'Maximul din lista este {maxim}')

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0 or numere[i] < 0:
        numere[i] *= -1
print('Noua lista este', numere)
