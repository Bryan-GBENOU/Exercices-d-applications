"""
Le programme demande n à l'utilisateur et calcule la somme de tous les nombres pairs compris
entre 1 et n.
"""
print("Le programme te permet de calculer la somme de tous les nombres pairs compris entre 1 et l'entier que vous aurez entré")
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
for i in range(0, n+1, 2):
    somme = somme + i
print(f"La sommme des nombres pairs de 1 à {n} est {somme}")