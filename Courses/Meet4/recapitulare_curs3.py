"""
Recapitulare - Curs3
"""
# o alta modalitate de a defini dictionare
another_dict = dict(name='John',
                    age=28,
                    email='john@123.com')
print(another_dict['email'])
print(another_dict.get('name'))
print(another_dict.keys())
print(another_dict.items())
another_dict.update({'married': True})
print(another_dict)

if 'phone' in another_dict:
    print('key found')
else:
    print('not found')
# ToDo - schimbare cheie dictionar folosind assert
# ToDo - sa folosim restul metodelor din dictionare
