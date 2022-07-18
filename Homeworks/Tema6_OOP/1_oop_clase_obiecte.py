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
print('==========================')

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
descrie()..
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
        aria = self.lungime * self.latime
        return f'Aria dreptunghiului este {aria.__round__(2)}'

    def perimetrul(self):
        perimetrul = self.lungime * 2 + self.latime * 2
        return f'Perimetrul dreptunghiului este {perimetrul.__round__(2)}'

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare


my_dreptunghi = Dreptunghi(3.3, 4, 'rosu')
print(my_dreptunghi.aria())
print(my_dreptunghi.perimetrul())
print(my_dreptunghi.schimba_culoare('negru'))
print('==========================')

"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""


class Angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele angajatului: {self.nume}')
        print(f'Prenumele angajatului: {self.prenume}')
        print(f'Salariul angajatului: {self.salariu}')

    def nume_complet(self):
        return f'{self.prenume} {self.nume}'

    def salariu_lunar(self):
        print(f'Salariul lunar al lui {self.nume_complet()} este {self.salariu}')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        return f'Salariul anual al lui {self.nume_complet()} este {salariu_anual}'

    def marire_salariu(self, procent_marire):
        self.salariu = self.salariu + (self.salariu * procent_marire / 100)
        print(f'Marirea de salariu este {procent_marire}% iar salariul a devenit {self.salariu}')


primul_angajat = Angajat('Ana', 'Maria', 8900)
primul_angajat.descrie()
print(primul_angajat.nume_complet())
primul_angajat.salariu_lunar()
print(primul_angajat.salariu_anual())
primul_angajat.marire_salariu(30)
print('==========================')

"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""


class Cont:
    iban = None
    titular_cont = None
    sold = 0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} Ron.')

    def debitare_cont(self, suma_debitata):
        if self.sold > 0 and self.sold > suma_debitata:
            self.sold = self.sold - suma_debitata
            print(f'Ati retras {suma_debitata} Ron si mai aveti {self.sold} Ron disponibili')
        else:
            print(f'Fonduri insuficiente!')

    def creditare_cont(self, suma_creditata):
        self.sold = self.sold + suma_creditata
        print(f'Contul a fost creditata cu suma de {suma_creditata} Ron si aveti in cont {self.sold} Ron')


cont1 = Cont('ING3773', 'Alex G.', 9900)
cont1.afisare_sold()
cont1.debitare_cont(700)
cont1.creditare_cont(300)