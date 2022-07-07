"""
Bubble sort
"""


def bubble_sort(lst):
    for i in range(0, (len(lst))):
        for j in range(0, (len(lst) - 1)):
            if lst[j] > lst[j + 1]:
                aux = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = aux
    return lst


lst = [1, 4, 3, 2, 5, 100, 87, 101, 45, 50, 1, 4, 5, 3, 5, 7, 4]
y = bubble_sort(lst)
print(y)
print()


# ToDo - sa migram exercitii anterioare in functii

def new_function(test_case_id, creator='Alex', emoji=':)'):
    print(f'running test case {test_case_id}')
    print(f'spirit by default when running is {emoji} for the creator {creator}')


if __name__ == '__main__':
    new_function(1)
print('============================')
# new_function() -> daca nu-i punem 'required' parametru ne va afisa eroare
new_function(3, 'Alexandru')
print('============================')
new_function(4, emoji=':(')
print('============================')
new_function(5, ':))')
print('============================')
print()


def another_function(*student):
    print(type(student))
    print(f'The youngest student is {student[0]}')


another_function('ionut', 'alex', 'vali', 'narcisa')
another_function('ionut')
print('============================')
print()


def last_function(**student):
    print(type(student))
    print(f'The youngest student is {student["nume"]}')
    print(f'The youngest student is {student["prenume"]}')
    print(f'The youngest student is {student["nota"]}')
    print(f'The youngest student is {student["mail"]}')


last_function(nume='Alex', prenume='Albon', nota=10, mail='alex@abc')
