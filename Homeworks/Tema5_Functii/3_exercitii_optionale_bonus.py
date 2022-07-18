"""
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune

Exemplu:
list1 = [1, 1, 2, 3]

list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""


def comun_list(list1, list2):
    list1_set = set(list1)
    list2_set = set(list2)
    if (list1_set & list2_set):
        print(list1_set & list2_set)


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
comun_list(list1, list2)


# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.

def reducere(pret_produs):
    x = int(input('Reducerea % este: '))
    if x > 100:
        print('Reducere invalida')
    else:
        reducerea = (x / 100) * pret_produs
        pretul = pret_produs - reducerea
        return f'Pretul redus este {pretul} ron'


print(reducere(100))

# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)

from datetime import datetime, date
import pytz


def data_ora_curenta(tara):
    tz = pytz.timezone(f'{tara}')
    country_current_datetime = datetime.now(tz)
    print(country_current_datetime)


data_ora_curenta('Europe/Bucharest')
data_ora_curenta('Asia/Shanghai')

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)
