"""
 Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat',
'Trabant', 'Opel']
"""

# 1.Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# ToDo - "FOR"
for i in range(len(masini)):
    print(f'Mașina mea preferată este {masini[i]}')
print('=========================================')

# ToDo -  "FOR-EACH"
for x in masini:
    print(f'Mașina mea preferată este {x}.')
print('==========================================')

# ToDo - "WHILE"
i = 0
while i < len(masini):
    print(f'Mașina mea preferată este {masini[i]}.')
    i += 1  # daca nu incrementam va fi un loop continuu
print('==========================================')

# 2.Aceeași listă:
# Folosește un for else În for
# - Modifică elementele din listă astfel încât să fie scrise cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in range(1, len(masini) - 1):
    masini[masina] = masini[masina].upper()
else:
    print(masini)
print('========================================')

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita de dvs! - MERCEDES')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam!')
print('========================================')

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# - Printează S-ar putea să vă placă mașina x.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    print('S-ar putea sa va placa masina', masina)
print('========================================')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        masini_vechi.append(masina)  # adaugare in lista creata
        index = masini.index(masina)  # pozitia valorilor Lastun si Trabant
        masini[index] = 'Tesla'  # suprascriem cu valoare Tesla in lista masini
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')
