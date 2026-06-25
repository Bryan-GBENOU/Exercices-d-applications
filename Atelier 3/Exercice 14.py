"""
Le programme affiche un cadre d'étoiles (uniquement le contour, l'intérieur est vide)
"""

def récupérer_saisie(message):
    while True:
        try:
            valeur = int(input(message))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Réalisons un cadre étoile (uniquement le contour, l'intérieur est vide) !\nPour se faire, entrez le nombre de ligne et de colonne souhaitée")

ligne = récupérer_saisie("Entrez le nombre de ligne : ")
colonne = récupérer_saisie("Entrez le nombre de colonne : ")

for i in range(ligne):
    if i == 0 or i == ligne - 1:
        print("*"*colonne)
    else:
        print("*" + " "*(colonne - 2) + "*")