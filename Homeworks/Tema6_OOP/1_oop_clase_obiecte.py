"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""
import math


class Cerc:
    # atribute
    raza = 0
    culoare = None

    # constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Culoarea cercului este {self.culoare}')
        print(f'Raza cercului este {self.raza}')

    def aria(self):
        aria = math.pi * self.raza ** 2
        return f'Aria este {aria.__round__(2)}'

    def diametru(self):
        diametru = self.raza * 2
        return f'Diametrul cercului este {diametru.__round__(2)}'

    def circumferinta(self):
        circumferinta = math.pi * self.raza * 2
        return f'Circumferinta cercului este {circumferinta.__round__(2)}'


cerc1 = Cerc(3, 'verde')
cerc1.descrie_cerc()

print(cerc1.aria())
print(cerc1.diametru())
print((cerc1.circumferinta()))
print('==========================')

cerc2 = Cerc(7, 'albastru')
cerc2.descrie_cerc()

print(cerc2.aria())
print(cerc2.diametru())
print(cerc2.circumferinta())

"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""


class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Lungimea este: {self.lungime}')
        print(f'Latimea este: {self.latime}')
        print(f'Culoarea este: {self.culoare}')

    def aria(self):
        return f'Aria dreptunghiului este {self.lungime * self.latime}'

    def perimetrul(self):
        return f'Aria dreptunghiului este {self.lungime * 2 + self.latime * 2}'

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare

