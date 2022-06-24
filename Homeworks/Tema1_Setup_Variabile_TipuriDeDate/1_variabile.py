"""
  Ex.1 Variabila este un loc din memorie care stocheaza valori (intregi, sir de caractere, float, boolean)
"""

# Ex_2 Declarare si initializare variabile
nume = "Gibson"  # string
nr_de_freturi = 22  # int
radius = 12.13  # float
goldtop = True  # boolean

# Ex_3 Functia "type" - pentru a verifica tipul de data
print(type(nume))
print(type(nr_de_freturi))
print(type(radius))
print(type(goldtop))

# Ex_4 Rotunjire 'float' folosind functia round()
print(round(radius))
print(type(radius))
radius = 12
print(type(radius))

# Ex_5 4 propozitii cu cele 4 variabile
print(nume + " este o marca de chitare foarte cunoscuta!")
print(f"Chitara are {nr_de_freturi} de freturi.")
print("Fingerboard radius este de", radius)
print(f"Sound-ul chitarei este {goldtop}")
