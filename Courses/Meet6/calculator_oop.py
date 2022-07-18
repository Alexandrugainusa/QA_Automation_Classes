"""
Curs6 - OOP
"""


class Calculator:
    def modulo(self):
        return 7 % 5

    def suma(self, a, b):
        return a + b

    def diferenta(self, a, b):
        return a - b

    def inmultire(self, a, b):
        return a * b

    def impartire(self, a, b):
        return a / b

    def my_magic_formula(self):
        return self.suma(3, 4) + self.diferenta(5, 2) + self.impartire(45, 9)

    def my_magic_formula2(self,a,b):
        return self.suma(a, b) + self.diferenta(a, b) + self.impartire(a, b)

my_calculator = Calculator()  # constructor default
a = my_calculator.suma(1, 5)
print(a)

b = my_calculator.diferenta(125, 25)
print(b)

c = my_calculator.inmultire(7, 8)
print(c)

d = my_calculator.impartire(21, 3)
print(d)

e = my_calculator.modulo()
print(e)

f = my_calculator.my_magic_formula()
print(f)

g = my_calculator.my_magic_formula2(6,2)
print(g)