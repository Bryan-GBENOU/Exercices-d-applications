"""
Le programme demande à l'utilisateur de saisir une liste de réels (taille <= 15) et effectue une rotation circulaire
: le premier élément devient le dernier, le second devient le premier, etc
"""
def recuperer_saisie_entier ():
    while True:
        try:
            valeur = int(input("Entrez la taille de cette liste : "))
            if 1 <= valeur <= 15:
                return valeur
            else:
                print("Veuillez entrer un nombre compris entre 1 et 15")
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

print("Ce programme vous permet de saisir une liste de réels (taille <= 15) et d'effectue une rotation circulaire:\
     le premier élément devient le dernier, le second devient le premier, etc")
liste = []
remplissage_liste(liste)
# utilisation de la méthode de slicing
résultat = liste[1:] + [liste[0]]
résultat_final = [f"{x:.5g}" for x in résultat]
print(f"Par rotation circulaire, on obtient donc {résultat_final}")