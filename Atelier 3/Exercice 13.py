"""
Le programme demande un nombre de lignes l à l'utilisateur et affiche un triangle d'étoiles
croissant.
"""
print("Réalisons un triangle étoile croissant !\nPour se faire, entrez le nombre de ligne souhaitée")
while True:
    try:
        ligne = int(input("Entrez le nombre de ligne : "))
        while ligne <= 0:
                print("Saisie invalide, veuillez réessayer")
                ligne = int(input("Entrez le nombre de ligne : "))
        break
    except ValueError:
        print("Erreur de saisir, veuillez recommencer")
for i in range(1, ligne + 1):
    print("*"*i)