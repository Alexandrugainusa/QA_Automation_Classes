"""
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
"""
# Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if-else
# Un IF-ELSE evalueaza daca o expresie este True sau False.

# Verifică și afișează dacă x este număr natural sau nu.
x = int(input('Introduce un numar natural: '))
if x >= 0:
    print(f'Numarul introdus este natural')
else:
    print('Numarul introdus nu este natural')

# Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x < 0:
    print('numarul este negativ')
elif x > 0:
    print('numarul este pozitiv')
else:
    print('numarul este neutru')

# Verifică și afișează dacă x este între -2 și 13.
if x >= -2 and x <= 13:
    print('numarul este intre -2 si 13')
else:
    print('numarul nu este in intervalul -2 si 13')

# Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y = int(input('Introduce al doilea numar: '))
if x - y < 5:
    print('Diferenta este mai mica de 5')
else:
    print('Diferenta este mai mare de 5')

# Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not (x >= 5 and x <= 27):
    print('Numarul ales nu este intre 5 si 27')
else:
    print('Numarul ales este intre 5 si 27')

# Verifică și afișează dacă x si y sunt egale, dacă nu afișează care din ele este mai mare
if x == y:
    print('x si y sunt egale')
elif x > y:
    print('x este mai mare decat y')
else:
    print('y este mai mare decat x')

# Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
verificare = input('Scrie o litera: ').lower()
if verificare == 'a' or verificare == 'e' or verificare == 'i' or verificare == 'o' or verificare == 'u':
    print('Litera introdusa este vocala')
else:
    print('Litera introdusa este consoana')

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = int(input("Nota ta este: "))
if nota >= 9 and nota <= 10:
    print('A')
elif nota >= 8 and nota < 9:
    print('B')
elif nota >= 7 and nota < 8:
    print('C')
elif nota >= 6 and nota < 7:
    print('D')
elif 4 < nota < 6:
    print('E')
elif 4 >= nota >= 1:
    print('F')
else:
    print('Nu ai introdus o nota de la 1 la 10')

