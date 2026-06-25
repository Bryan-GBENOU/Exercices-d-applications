"""Le programme demande un nombre de lignes l et un nombre de colonnes c, puis affiche un rectangle plein d'étoiles."""
print("Réalisons un rectangle étoile !\nPour se faire entrez le nombre de ligne et de colonne que vous souhaitez")

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

ligne = récupérer_saisie("Entrez le nombre de ligne : ")
colonne = récupérer_saisie("Entrez le nombre de colonne : ")
for i in range(ligne):
    print("*"*colonne)    