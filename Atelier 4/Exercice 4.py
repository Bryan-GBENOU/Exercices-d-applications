"""
Le programme demande à l'utilisateur de saisir deux listes de même longueur, puis crée une troisième liste
dont chaque élément est la somme des éléments correspondants des deux premières
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

print("Ce programme vous permet de créer deux listes d'entier et affiche une troisième liste qui est la somme des éléments correspondants des deux premières listes")
print("Remplissez la première liste :")
liste1 = []
remplissage_liste(liste1)
print("Remplissez la seconde liste :")
liste2 = []
remplissage_liste(liste2)
liste_1_2 = list(zip(liste1, liste2))
liste_des_sommes = []
for a, b in liste_1_2:
    liste_des_sommes.append(a + b)
liste_somme = [f"{x:.5g}" for x in liste_des_sommes]
print(f"La liste des sommes des éléments correspondants de vos deux listes donne {liste_somme}")