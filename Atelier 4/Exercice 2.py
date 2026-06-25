"""
Le programme :
• Demande à l'utilisateur de saisir n valeurs dans une liste
• Après la saisie, trouve la plus grande valeur et affiche sa position dans la liste
"""
def recuperer_saisie_entier ():
    while True:
        try:
            valeur = int(input("Entrez la taille de cette liste : "))
            while valeur <= 0:
                print("Saisie invlide, veuillez réessayer")
                valeur = int(input("Entrez la taille de cette liste : "))
            return valeur
        except ValueError:
            print("L'élément que vous avez entré est invalide, veuillez réessayer")

def remplissage_liste (liste):
    taille = recuperer_saisie_entier()
    for i in range(taille):
        try:
            valeur = float(input("Entrez un élément de cette liste : "))
            liste.append(valeur)
        except ValueError:
            print("L'élément que vous avez entré est invalide, veuillez réessayer")
    return(liste)
print("Ce programme vous permet de créer une liste d'entier et d'affiche le grand nombre et sa position dans la liste")
print("Pour ce faire, remplissez la liste :")
liste = []
remplissage_liste(liste)
print(f"Le maximum est {max(liste):.5g} et est à la position {liste.index(max(liste))}")