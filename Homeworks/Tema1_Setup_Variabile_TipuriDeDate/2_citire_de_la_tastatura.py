"""
    From input
"""

# Ex_6 Afiseaza 'Numele comlet are x caractere.'
nume = input("Name: ")
prenume = input("Prename: ")
print(f"Numele complet are {len(nume + prenume)} caractere.")

# Ex_7 Aria dreptunghiului este x.

lungimea = float(input('Lungimea este: '))
latimea = float(input('Latimea este: '))
arie_dreptunghi = lungimea * latimea
print("Aria dreptunghiului este", arie_dreptunghi)

# Ex_8 Afișează stringul fără ultimele x caractere.
expression = "Coral is either the stupidest animal or the smartest rock"
cut = int(input('Final cut: '))
print(expression[:-cut])

# Ex_9 declară un string nou care să fie format din primele 5 caractere + ultimele 5;
print(expression[0:5] + expression[-5:])

# Ex_10 afișează de câte ori apare cuvântul 'the';
print(expression.count("the"))

# Ex_11 înlocuiește ‘the’ cu ‘THE’ peste tot - printează rezultatul;
print(expression.replace("the", "THE"))

# Ex_12 salvează într-o variabilă și afișează indexul de start al cuvântului ‘rock’;
print(expression.find("rock"))
rock_at_index = 53

print(expression[:rock_at_index])
