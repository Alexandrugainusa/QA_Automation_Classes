"""
joc
"""
import random

numar_secret = random.randint(1, 30)
numar_ghicit = int(input("Alege un numar intre 1 & 30: "))
while numar_ghicit != numar_secret:
    numar_ghicit = int(input("Mai alege o data: "))
if numar_ghicit < numar_secret:
    print('Alege un numar mai mare')
elif numar_ghicit > numar_secret:
    print('Alege un numar mai mic')
else:
    print("Ai ghicit!")
