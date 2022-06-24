"""
Structuri de date

"""

# getText - extrage text

my_variable = "Dreptunghi"
print(my_variable[0])  # afiseaza primul caracter din string
print(my_variable[-1])  # afiseaza ultimul caracter din string
print(my_variable[-3])  # afiseaza antepenultimul caracter din string
print(len(my_variable))  # afiseaza cate caractere contine stringul
print(my_variable[len(my_variable) - 1])  # afiseaza ultimul caracter din string

# Slicing - [start:end]

print(my_variable[0:])  # afiseaza tot stringul
print(my_variable[:3])  # Dre
print(my_variable[2:])  # eptunghi
print(my_variable[3:6])  # ptu

# Slicing - [start:stop:step-over]

print(my_variable[0:10:2])  # afiseaza caracterele din 2 in 2 / Detnh
print(my_variable[::-1])  # afiseaza stringul invers
print(my_variable[::-2])  # afiseaza stringul invers din 2 in 2
print(my_variable.upper())  # afiseaza stringul cu litere mari

print(my_variable.find("e"))  # afiseaza indexul lui "e"

my_variable = "Dreptunghiul lui Matei"
print(my_variable.replace("Matei", "Vasile"))

# Split

print(my_variable.split(' '))  # desparte stringul in 3 stringuri
print(my_variable.split(' ')[0])  # desparte stringul si il afiseaza doar pe cel de la index 0 - "Dreptunghiul"
print(my_variable.split(' ')[0][1:3])  # din primul string afisat, ia caracterele de la 1 la 3 - "re"

# Imutabilitate
# my_variable[0] = "T"
# print(my_variable) - putem sa-l feliem dar NU PUTEM SA-L SCHIMBAM (apare eroare in consola)

