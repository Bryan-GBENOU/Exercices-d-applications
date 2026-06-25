"""
Le programme permet à l'utilisateur de saisir une liste de réels (taille <= 30), puis la trie par ordre
décroissant.
Il le fait de deux façons :
• Avec sort(reverse=True)
• En implémentant manuellement le tri à bulles (bubble sort)
"""
def recuperer_saisie_entier ():
    while True:
        try:
            valeur = int(input("Entrez la taille de cette liste : "))
            if 1 <= valeur <= 30:
                return valeur
            else:
                print("Veuillez entrer un nombre compris entre 1 et 30")
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

print("Ce programme vous permet de créer une liste d'entier et de la trier par ordre décroissant")
print("Pour ce faire, remplissez la liste :")  
liste = []
remplissage_liste(liste)
liste_entier = [f"{x:.5g}" for x in liste]
liste_entier.sort(reverse=True)
print(f"Après rangement on obtiens : {liste_entier}")