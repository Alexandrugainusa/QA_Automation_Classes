"""
2. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random.
Ne imaginam că dăm cu zarul și salvăm acest număr în dice_roll.

Ia un număr ghicit de la utilizator.
Verifică și afișază dacă utilizatorul a ghicit 3 opțiuni:
- Ai pierdut. Ai ales un număr mai mic. Ai ales x dar a fost y.
- Ai pierdut. Ai ales un număr mai mare. Ai ales x dar a fost y.
- Ai ghicit. Felicitări? Ai ales x și zarul a fost y.
"""
import random

dice_roll = random.randint(1, 6)
x = int(input("Ghiceste zarul: "))
if x < dice_roll:
    print(f'Ai pierdut. Ai ales un număr mai mic. Ai ales {x} dar a fost {dice_roll}.')
elif x> dice_roll:
    print(f'Ai pierdut. Ai ales un număr mai mare. Ai ales {x} dar a fost {dice_roll}.')
else:
    print(f'Ai ghicit. Felicitări? Ai ales {x} și zarul a fost {dice_roll}.')