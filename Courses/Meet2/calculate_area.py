"""
Afiseaza aria - Curs2

"""
import math

figure: str = input('Enter your figure (circle, square, rectangle, polygon): ')

if figure.lower() == "circle":  # poate sa ia input-ul in orice caz: (ex: "CirCLe")
    # Aria cercului
    r = float(input('Introduce raza: '))
    circle_area = math.pi * r ** 2
    print(round(circle_area, 2))  # setam sa apara 2 zecimale dupa virgula
elif figure.lower() == 'square':
    s = float(input('Introduce latura patratului: '))
    if s <= 0:
        print('Nu se poate calcula aria')
    else:
        square_area = s ** 2
        print(round(square_area, 2))
elif figure.lower() == 'polygon':  # poligon regulat
    p = float(input('Introduce numarul de laturi: '))
    l = float(input('Introduce lungimea laturii: '))
    if p <= 0:
        print('Nu se poate calcula aria')
    else:
        polygon_area = (1 / 4) * p * (l ** 2) * (1 / math.tan(math.pi / p))
        print(round(polygon_area, 2))
else:
    # Aria dreptunghiului
    L = float(input('Lungimea dreptunghiuli este: '))
    l = float(input('Latimea dreptunghiului este '))
    rectangle_area = L * l
    print(round(rectangle_area, 2))
