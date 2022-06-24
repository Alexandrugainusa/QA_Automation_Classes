"""
- Afișează doar numerele pare;
- Afișează doar numerele impare;
- hint: folosește slicing, controlează din pas.
"""
str = '0123456789'
# nr pare
print(str[0::2])
# nr impare
print(str[1::2])

# afișează caracterul din mijloc.
# cuvant = input("String impar: ")
# middle = len(cuvant)//2
# print(cuvant[middle])

# verifică dacă un string este palindrom.
# expected_str = "capac"
# palindrom = input("Word: ")
# assert palindrom == expected_str
# if palindrom == palindrom[::-1]:
#     print("este palindrom")
# else:
#     print("nu este palindrom")

# Folosind o singură linie de cod :
# citește un string de la tastatură (ex: 'alabala portocala');
# salvează fiecare cuvânt într-o variabilă;
# word = input("Enter -> alabala portocala: ").split()
# print(word)

word = input("Enter: ")
x = word[0]
print(x)
y = word.replace(x, x.upper())
print(y[0].replace(y[0], y[0].lower()) + y[1:-1] + y[-1].replace(y[-1], y[-1].lower()))
