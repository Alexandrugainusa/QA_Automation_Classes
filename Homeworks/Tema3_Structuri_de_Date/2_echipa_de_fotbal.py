"""
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea

- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
"""

jucatori = ["Jucator1", "Jucator2", "Jucator3", "Jucator4", "Jucator5"]
print('ECHIPA DE FOTBAL ESTE', jucatori)
SCHIMBARI_MAXIME = 3
schimbari_efectuate = 1
schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
jucator_intrat = "Jucator6"
jucator_iesit = "Jucator3"

if jucator_iesit in jucatori and schimbari_ramase > 0:
    if jucator_intrat in jucatori:
        print('Jucatorul este deja in teren')
    else:
        jucatori.remove(jucator_iesit)
        jucatori.append(jucator_intrat)
        schimbari_ramase -= 1
        print(f'Se cere schimbare de la margine!')
        print(f'A intrat {jucator_intrat}, a iesit {jucator_iesit}, mai ai {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <= 0:
        print('Nu mai poti face schimbari!')
    else:
        print(f'nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren')
        print(f'Mai ai {schimbari_ramase} schimbari')
print(f'ACTUALA ECHIPA DE FOTBAL ESTE {jucatori}')
