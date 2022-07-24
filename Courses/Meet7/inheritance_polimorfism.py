"""
Curs 7.2 Inheritance & Polimorfism.
"""


# clasa parinte
class Chef:
    def make_steak(self):
        print('medium rare steak')

    def make_omleta(self):
        print('tasty omleta')


# clase copil
class RomanianChef(Chef):
    def make_sarmale(self):
        print('sarmale cu smantana')

    def make_mici(self):
        print('mici cu mustar')

    def make_omleta(self):  # suprascriem metoda din clasa parinte - polimorfism
        print('omleta se mananca cu slanina')


class HungarianChef(Chef):
    def make_gulash(self):
        print('gulash picant')

    def make_kurtosh(self):
        print('kurtosh dulce cu nutella si nuca')

    def make_omleta(self):  # - polimorfism
        print('omleta cu oua de rata')


class MoldavianChef(RomanianChef):
    def make_hrisca(self):
        print('se fierbe cu ulei')


if __name__ == '__main__':
    # creare obiecte
    chef = Chef()
    romanian_chef = RomanianChef()
    hungarian_chef = HungarianChef()
    moldavian_chef = MoldavianChef()

    # apelam metodele
    chef.make_omleta()
    romanian_chef.make_sarmale()
    hungarian_chef.make_gulash()
    moldavian_chef.make_mici()

    # POLIMORFISM - overriding
    chef.make_omleta()
    romanian_chef.make_omleta()
    hungarian_chef.make_omleta()
