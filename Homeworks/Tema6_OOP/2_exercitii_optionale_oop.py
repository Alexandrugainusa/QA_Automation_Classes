"""
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs  | cantitate | preț bucată | Total
Telefon |    7      |    700      | 49000
"""
from datetime import date


class Factura:
    SERIA = 'AA'
    numar = 0
    nume_produs = None
    cantitate = 0
    pret_buc = 0

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, noua_cantitate):
        self.cantitate = noua_cantitate
        print(f'Noua cantitate este {self.cantitate}')

    def schimba_pret(self, noul_pret):
        self.pret_buc = noul_pret
        print(f'Noul pret este {self.pret_buc}')

    def schimba_nume_produs(self, nume_produs_nou):
        self.nume_produs = nume_produs_nou
        print(f'Noul nume al produsului este {self.nume_produs}')

    def genereaza_factura(self):
        total = self.cantitate * self.pret_buc
        print(f'Factura seria: {self.SERIA}  numar: {self.numar}')
        today = date.today()
        print(f'Data: {today}')
        print(f'Produs  |     Cantitate    |    Pret bucata  |   Total')
        print(f'{self.nume_produs} |        {self.cantitate}         |           {self.pret_buc}   |    {total}')


factura1 = Factura(3, 'Telefon', 7, 700)
factura1.genereaza_factura()
print('=======================================================')

"""
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""


class Masina:
    marca = 'Honda'
    model = None
    viteza_maxima = 0
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'verde', 'mov', 'galben', 'albastru', 'portocaliu', 'rosu', 'crem'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Marca masinii este {self.marca}')
        print(f'Modelul: {self.model}')
        print(f'Viteza maxima: {self.viteza_maxima} km/h')
        print(f'Viteza actuala: {self.viteza_actuala} km/h')
        print(f'Culoarea din fabrica: {self.culoare}')
        print(f'Masina este inmatriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        print(f'Masina cumparata este inmatriculata: {self.inmatriculata}')

    def vopseste(self, noua_culoare):
        if noua_culoare in self.culori_disponibile:
            self.culoare = noua_culoare
            print(f'Noua culoare a masinii dvs este {self.culoare}')
        else:
            print(f'Culoarea {noua_culoare} nu este disponibila ptr masina dvs!')

    def accelereaza(self, viteza):
        if viteza < self.viteza_actuala:
            print('Eroare, inca nu ai bagat in viteza!')
        elif viteza <= self.viteza_maxima:
            self.viteza_actuala = viteza
            print(f'Accelerare pana la viteza {self.viteza_actuala} km/h')
        else:
            self.viteza_actuala = self.viteza_maxima
            print(f'Ai atins viteza maxima de {self.viteza_actuala} km/h')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Masina franeaza si se opreste avand viteza stationarii de {self.viteza_actuala} km/h')


masina1 = Masina('Shadow', 180)
masina1.descrie()
masina1.inmatriculare()
masina1.vopseste('negru')
masina1.vopseste('portocaliu')
masina1.accelereaza(120)
masina1.accelereaza(-3)
masina1.accelereaza(280)
masina1.franeaza()
print('=======================================================')

"""
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""


class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        print(f'Lista task-ui: {self.todo}')

    def finalizeaza_task(self, nume):
        self.todo[nume] = self.todo.pop(nume)
        print(f'Task-ul {self.todo[nume]} a fost finalizat!')
        print(f'Lista actualizata: {self.todo}')

    def afiseaza_todo_list(self):
        print(f'{self.todo.keys()}')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo.keys():
            print(f'Detaliile task-ului sunt: {self.todo.get(nume_task)}')
        else:
            print(f'Doriti sa adaugati {nume_task} in lista?')
            raspuns = True
            if raspuns == False:
                print(f'Nu stiti inca')
            else:
                self.todo['Canta'] = 'Gama Do major'
                print(f'Lista actualizata: {self.todo}')


lista1 = TodoList()
lista1.adauga_task('Sport', 'Wushu')
lista1.adauga_task('Scrie', 'Poezie')
lista1.adauga_task('Python', 'OOP')
lista1.finalizeaza_task('Python')
lista1.afiseaza_todo_list()
lista1.afiseaza_detalii_suplimentare('Scrie')
lista1.afiseaza_detalii_suplimentare('Canta')
