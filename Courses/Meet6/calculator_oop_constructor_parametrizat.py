"""
OOP - constructor cu parametri
"""


class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def modulo(self):
        return 7 % 5

    def suma(self):
        return self._a + self._b

    def diferenta(self, a, b):
        return a - b

    def inmultire(self, a, b):
        return a * b

    def impartire(self):
        return self._a / self._b

    def my_magic_formula(self):
        return self.suma() + self.diferenta(5, 2) + self.impartire()

    def my_magic_formula2(self, a, b):
        return self.suma() + self.diferenta(a, b) + self.impartire()


my_calculator = Calculator(3, 4)  # constructor cu parametri
print(my_calculator.suma())

b = my_calculator.diferenta(125, 25)
print(b)

c = my_calculator.inmultire(7, 8)
print(c)

d = my_calculator.impartire()
print(d)

e = my_calculator.modulo()
print(e)

f = my_calculator.my_magic_formula()
print(f)

g = my_calculator.my_magic_formula2(6, 2)
print(g)

# ToDo - sa cream o noua clasa Calculator sa folosim si alte operatii
#  -> sin, cos, radical, la puteara a 2-a , factorial