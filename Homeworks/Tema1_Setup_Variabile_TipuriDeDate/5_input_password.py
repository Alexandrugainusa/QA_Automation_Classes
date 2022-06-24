"""
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
"""

pwd = input('Please enter again the pass: ')
for i in pwd:
    if i.replace(pwd, '*'):
        print('*', end='')
    else:
        print(i, end='')
