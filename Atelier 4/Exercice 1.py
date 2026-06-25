"""
À partir de deux listes saisies par l'utilisateur, le programme calcule leur produit scalaire : S (liste1[i] x liste2[i])
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

print("Calculons le produit scalaire de deux listes d'entier que vous saisirez")
print("Remplissez la première liste :")
liste1 = []
remplissage_liste(liste1)
liste2 = []
remplissage_liste(liste2)
liste_1_2 = list(zip(liste1, liste2))
liste_des_multiplication = []
for a, b in liste_1_2:
    liste_des_multiplication.append(a * b)
produit_scalaire = sum(liste_des_multiplication)
print(f"Le produis scalaire de vos deux listes donne {produit_scalaire:.5g}")