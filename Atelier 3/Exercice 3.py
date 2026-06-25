"""
Le programme demande un entier n et calcule la somme 1 + 2 + 3 + ... + n.
• Avec une boucle for
• Avec la formule mathématique (n*(n+1))/2
"""
print("Le programme te permet de calculer la somme 1 + 2 + 3 + ... + n d'un entier")
while True:
    try:
        n = int(input("Entrez votre nombre, nous calculerons la somme : "))
        while n < 1:
            print("Saisie invalide, veuillez réessayer")
            n = int(input("Entrez votre nombre, nous calculerons la somme : "))
        break
    except ValueError:
        print("Saisie invalide, veuillez réessayer")
somme = 0
for i in range(1, n+1):
    somme = somme + i
print(f"La somme de 1 à {n} est {somme}")
print(f"{(n*(n+1))/2:.5g}")