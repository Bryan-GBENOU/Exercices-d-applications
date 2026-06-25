"""
Le programme :
• Demande la taille du tableau (<= 45)
• Saisit les valeurs
• Calcule la moyenne
• Affiche le nombre de valeurs supérieures ou égales à la moyenne
"""
def recuperer_saisie_entier ():
    while True:
        try:
            valeur = int(input("Entrez la taille de cette liste : "))
            if 1 <= valeur <= 45:
                return valeur
            else:
                print("La taille doit être un entier entre 1 et 45, veuillez réessayer")
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
print("Ce programme vous permet de créer une liste d'entier et d'afficher le nombre de valeur supérieur ou égale à la moyenne")
print("Pour ce faire, remplissez la liste :")  
liste = []
remplissage_liste(liste)
moyenne = sum(liste) / len(liste)
compteur = 0
for i in liste:
    if i >= moyenne:
        print(f"{i:.5g} est supérieur ou égal à la moyenne {moyenne:.5g}")
        compteur += 1
print(f"Il y a {compteur} valeurs supérieur ou égal à la moyenne {moyenne:.5g}")