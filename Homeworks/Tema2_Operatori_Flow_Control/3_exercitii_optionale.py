"""
Exercitii optionale

5. X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
"""

x = float(input('Introduce primul unghi din triunghi: '))
y = float(input('Introduce al doilea unghi din triunghi: '))
z = float(input('Introduce al treilea unghi din triunghi: '))
# conditie: x + y + z = 180
if x + y + z == 180 and x > 0 and y > 0 and z > 0 and x != 180 and y != 180 and z != 180:
    print('Triunghiul este valid')
else:
    print('Nu este triunghi valid')
