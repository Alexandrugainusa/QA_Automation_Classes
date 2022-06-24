"""
Exercitii optionale
"""

# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input("Numarul tau X este: "))
if 999 < x <= 9999:
    print(f'{x} are 4 cifre')
else:
    print(f'{x} nu are minim 4 cifre')

# 2.Verifică dacă x are exact 6 cifre.
if 99999 < x <= 999999:
    print(f'{x} are exact 6 cifre')
else:
    print(f'{x} nu are 6 cifre')

# 3.Verifică dacă x este număr par sau impar (x e int).
if x % 2 == 0:
    print(f'{x} este par')
else:
    print(f'{x} este impar')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
y = int(input("Numarul tau Y este: "))
z = int(input("Numarul tau Z este: "))
if x > y > z:
    print(f'{x} este mai are decat {y} si {z}')
elif y > x > z:
    print(f'{y} este mai are decat {x} si {z}')
elif z > y > x:
    print(f'{z} este mai are decat {x} si {y}')
elif x == y == z:
    print(f'Numerele sunt egale')
elif x == y:
    if x > z:
        print(f'x si y sunt egale si mai mari decat z')
    else:
        print(f'z este mai mare decat x si y')
elif y == z:
    if y > x:
        print(f'y si z sunt egale si mai mari decat x')
    else:
        print(f'x este mai mare decat y si z')
elif z == x:
    if z > y:
        print(f'x si z sunt egale si mai mari decat y')
    else:
        print(f'y este mai mare decat x si z')


