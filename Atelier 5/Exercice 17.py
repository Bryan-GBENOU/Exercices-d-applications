"""
Le programme contient la fonction schtroumpf(lst1, lst2) qui retourne le produit scalaire des deux listes
"""
def schtroumpf(liste1, liste2):
    liste_1_2 = list(zip(liste1, liste2))
    liste_des_multiplication = []
    for a, b in liste_1_2:
        liste_des_multiplication.append(a * b)
    produit_scalaire = sum(liste_des_multiplication)
    return produit_scalaire

def remplissage_liste(liste):
    taille = récuperation_saisie_entier("Quelle est la taille souhaitée pour votre liste ?\n")
    for i in range(taille):
        élément = récuperation_saisie_float("Entrez un élément de la liste : ")
        liste.append(élément)
    return liste

def récuperation_saisie_entier(message): #principalement utiliser pour la taille du tableau
    while True:
        try:
            valeur = int(input(message))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_float(message): #principalement utiliser pour les éléments du tableau
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Calculons le produit scalaire de deux listes d'entier que vous saisirez")
print("Remplissez la première liste :")
liste1 = []
remplissage_liste(liste1)
print("Remplissez la seconde liste :")
liste2 = []
remplissage_liste(liste2)
print(f"Le produis scalaire de vos deux listes donne {schtroumpf(liste1, liste2):.5g}")
