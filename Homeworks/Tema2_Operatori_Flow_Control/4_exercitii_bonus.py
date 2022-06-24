"""
1.Verificare îmbarcare persoane
Ține minte următoarele date:
- Vârstă;
- Însoțit de mama;
- Însoțit de tata;
- Pașaport;
- Act permisiune mama;
- Act permisiune tata.
Condiții de îmbarcare
- Dacă pers are vârstă peste 18 ani și are pașaport.
- Dacă pers are sub 18 ani, are pașaport și e însoțită de ambii părinți.
- Dacă pers are sub 18 ani, are pașaport, e însoțită de cel puțin un părinte
și are permisiune în scris de la celalat părinte.
● Aici vreau să testezi codul cu toate variantele posibile.
● Să generezi cazuri de test și expected result, apoi să rulezi codul și să
completezi actual results.
Ex:
Vârstă 19 ani, nu am pașaport => Nu mă pot îmbarca.
Vârstă 17 ani, am pașaport, ambii părinți => Mă pot îmbarca.
Etc
"""

varsta = int(input("Varsta dumneavoastra este: ").lower())
pasaport = input("Aveti pasaport? ")
if 0 < varsta < 18 and pasaport.lower() == 'da':
    print('Urmariti formularul de imbarcare!')
    mama = input('Calatoriti cu mama? Raspuns: ')
    tata = input('Calatoriti cu tata? Raspuns:')
    if mama == 'nu':
        act_mama = input('Aveti permisiunea de la mama? Raspuns: ')
    elif tata == 'nu':
        act_tata = input('Aveti permisiunea de la tata? Raspuns: ')
    if mama and tata == 'da':
        print('Minor cu ambii parinti. Puteti sa va imbarcati!')
    elif mama == 'da' and tata == 'nu' and act_tata == 'da':
        print('Minor cu mama si act de la tata. Puteti sa va imbarcati!')
    elif tata == 'da' and mama == 'nu' and act_mama == 'da':
        print('Minor cu tata si act de la mama. Puteti sa va imbarcati!')
    else:
        print("Nu va puteti imbarca! Va asteptam la anul viitor!")
elif varsta >= 18 and pasaport == 'da':
    print('Va puteti imbarca!')
else:
    print('Nu va puteti imbarca! Va asteptam la anul viitor!')
