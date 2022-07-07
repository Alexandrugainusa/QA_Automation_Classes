"""
1.Funcție care să calculeze și să returneze suma a două numere
"""


def addition(a, b):
    return f'Sum = {a + b}'


result = addition(3, 4)
print(result)


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def even_or_odd(x):
    if x % 2 == 0:
        print('Your number is even - ', True)
    print('Your number is odd - ', False)  # nu am mai avea nevoie de conditia 'else'


even_or_odd(5)


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
def all_the_characters(name, prename, middle_name):
    complete_name = (name + prename + middle_name)
    complete_name = complete_name.replace(' ', '')
    return len(complete_name)


print(all_the_characters('Gainusa', 'Alexandru', 'Catalin'))


# 4. Funcție care returnează aria dreptunghiului
def area_rectangular(L, l):
    area = L * l
    return area


print(area_rectangular(3, 4))

# 5. Funcție care returnează aria cercului
import math


def circle_area(r):
    area = math.pi * r ** 2
    return area


print(circle_area(5))


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
def find_character(my_string):
    if 'x' in my_string:
        return True
    return False


print(find_character('atrx'))


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
def lower_upper(my_string):
    char_upper = 0
    char_lower = 0
    for char in my_string:
        if char.isupper():
            char_upper += 1
        elif char.islower():
            char_lower += 1
    print(f'Nr de caractere mari {char_upper}')
    print(f'Nr de caractere mici {char_lower}')


lower_upper('abcdABC')

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive
lst = [1, 3, 4, -6, 7, -8, 10, -11, 13, 17, -12, -24]


def positive_numbers(my_list):
    my_list_positive = []
    for number in my_list:
        if number > 0:
            my_list_positive.append(number)
    return my_list_positive
    # print(f'List with positive numbers {lst2}')


print(positive_numbers(lst))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

