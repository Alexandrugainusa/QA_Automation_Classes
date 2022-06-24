"""
Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o:
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
"""

musical_notes = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]  # lista note muzicale
print(musical_notes)
notes = musical_notes[::-1]  # inversare lista folosind slicing
print(notes)

print(list(reversed(notes)))

# De câte ori apare ‘do’?
print(musical_notes.count("do"))

lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]

# Găseste 2 variante să le unești într-o singură listă.
combined = lista_1 + lista_2
print(combined)

final_list = [*lista_1, *lista_2]
print(final_list)

# for x in lista_2:
#     lista_1.append(x)
# print(lista_1)

# lista_1.extend(lista_2)
# print(lista_1)

# Sortează și afișază lista generată la exercițiul anterior.
print(sorted(final_list))

# lista_1.sort(reverse=False)
# print(lista_1)

# Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
if final_list:
    print("List is not empty")
else:
    print("List is empty")

# Folosește o funcție care să șteargă lista
final_list.clear()
print(final_list)

# Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if final_list:
    print("List is not empty")
else:
    print("List is empty")

# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())
# for key in dict1:
#     print(key)

# Printează cei 3 elevi și notele lor
print(f'Ana a luat nota {dict1["Ana"]}.')
print(f'Gigel a luat nota {dict1["Gigel"]}.')
print(f'Dorel a luat nota {dict1["Dorel"]}.')

# Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1["Dorel"] = 6
print(dict1)

# Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
del dict1["Gigel"]
print(dict1)
dict1["Ionica"] = 9
print(dict1)

# Set -colectie neordonata de iteme, care nu poate avea duplicate si nu le putem accesa folosind indexul
# Adaugă în zilele_sapt ‘luni’
# Afișeaza zile_sapt
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămâni.')
else:
    print('Weekend nu este un subset al zilelor din săptămâni.')

# x = weekend.issubset(zile_sapt)
# print(x)

# Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt - weekend)

# Afișază intersecția elementelor din aceste 2 seturi.
print(zile_sapt & weekend)
