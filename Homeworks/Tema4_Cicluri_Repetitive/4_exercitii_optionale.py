"""
Exercitii Optionale
1.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
"""
import random

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')
print('===================================================')

# 2.Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for i in range(len(alte_numere)):
    for j in range(len(alte_numere) - 1):
        if alte_numere[j] > alte_numere[j + 1]:
            alte_numere[j], alte_numere[j + 1] = alte_numere[j + 1], alte_numere[j]
print(f'Lista sortata este: {alte_numere}')
print('===================================================')

#3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!

numar_secret = random.randint(1,30)
numar_ghicit = int(input("Alege un numar intre 1 & 30: "))
while numar_ghicit != numar_secret:
    numar_ghicit = int(input("Mai alege o data: "))
    if numar_ghicit < numar_secret:
        print("Ai ales un numar mai mic!")
    elif numar_ghicit > numar_secret:
        print("Ai ales un numar mai mare!")
    else:
        print('Felicitari! Ai ghicit numarul!')
print('==================================================')

# numar_secret = random.randint(1,30)
# condition = True
# while condition:
#     numar_ghicit = int(input("Alege un numar intre 1 & 30: "))
#     if numar_ghicit == numar_secret:
#         print("Ai ghicit")
#         break
#     else:
#         print('Mai introduce o data')



# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777

numar = int(input("Choose the number: "))
for i in range(numar + 1):
    for j in range(i):
        print(i, end='')
    print('')
print('===================================================')

# 5.tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')
