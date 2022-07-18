"""
1. Funcție care primește o lună din an și returnează câte zile are acea luna
"""

calendar = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}


def days(months):
    return calendar.get(months)


print(days("January"))
print(days('March'))
print('=================================')
print()


# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

def calculator(nr1, nr2):
    a = nr1 + nr2
    b = nr1 - nr2
    c = nr1 * nr2
    d = nr1 / nr2
    return a, b, c, d


a, b, c, d = calculator(100, 10)
print(f'Suma : {a}')
print(f'Diferenta : {b}')
print(f'Inmultirea : {c}')
print(f'Impartirea : {d}')
print('=================================')

a, b, c, d = calculator(10, 2)
print(f'Suma : {a}')
print(f'Diferenta : {b}')
print(f'Inmultirea : {c}')
print(f'Impartirea : {d}')
print('=================================')
print()


# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def list_number(number):
    my_dict = {}
    for i in range(0, 10):
        my_dict[i] = number.count(i)
    return my_dict


lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(list_number(lista))
print('=================================')


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def max_min(x, y, z):
    if x > y and x > z:
        return x
    if y > z and y > x:
        return y
    if z > x and z > y:
        return z


print(max_min(3, 5, 7))
print(max_min(4, 25, 2))
print('=================================')


# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def sum_nr(nr):
    suma = 0
    for i in range(0, nr + 1):
        suma += i
    return suma


x = sum_nr(4)
print(f'Suma tuturor numerelor este : {x}')

