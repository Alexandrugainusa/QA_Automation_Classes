"""
2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
împreună).
- ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
- INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

- ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
- POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""

from abc import ABC, abstractmethod


# abstraction
class FormaGeomatrica(ABC):
    PI = 3.14  # constanta

    @abstractmethod
    def aria(self):
        raise NotImplemented

    def descrie(self):
        print(f'Cel mai probabil am colturi')


# inheritance
class Patrat(FormaGeomatrica):  # inheritance + encapsulation
    __latura = 0  # variabila latura este PRIVATE

    # definire constructor cu latura
    def __init__(self, latura):
        self.__latura = latura

    @property  # este un decorator, metoda Pytho, care ne ajuta sa folosim getter/setter/deleter
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Latura are lungimea: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Noua lungimea a laturii este: {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Se sterge valoarea laturii.')
        self.__latura = 0

    def aria(self):  # metoda abstracta din clasa parinte, cu logica din clasa PATRAT (clasa copil)
        self.aria = self.__latura ** 2
        return self.aria


class Cerc(FormaGeomatrica):  # inheritance + encapsulation
    __raza = 0

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Noua raza este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Se sterge valoarea razei.')
        self.__raza = 0

    def aria(self):  # metoda abstracta din clasa parinte, cu logica din clasa CERC
        aria_cercului = self.__raza ** 2 * self.PI
        return aria_cercului.__round__(2)

    def descrie(self):  # POLIMORFISM - metoda din clasa parinte care se suprascrie
        print(f'Eu nu am colturi.')


patrat1 = Patrat(3)  # obiectul patrat1 de tip Patrat
patrat1.descrie()  # accesam metoda DESCRIE din clasa parinte FormaGeometrica
print(patrat1.aria())
patrat1.latura  # get latura
patrat1.latura = 7  # set latura
del patrat1.latura  # deleter
print('================================')

cerc1 = Cerc(3)
cerc1.descrie()
print(cerc1.aria())
cerc1.raza  # getter
cerc1.raza = 5  # setter
del cerc1.raza  # deleter
