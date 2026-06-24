"""
Le programme contient la fonction copier_liste(original) qui retourne une copie de la liste passée en
paramètre
"""
def copier_liste(liste_originale):
    copie = liste_originale[:] #utilisation du slicing : [:] signifie les éléments de la liste du début à la fin
    return copie

def remplissage_liste(liste):
    taille = récuperation_saisie_entier("Quelle est la taille souhaitée pour votre liste ?\n")
    for i in range(taille):
        élément = récuperation_saisie_float("Entrez un élément de la liste : ")
        liste.append(élément)
    return liste

def récuperation_saisie_entier(message):# le paramètre message est dans la fonction remplissage_liste()
    while True:
        try:
            valeur = int(input(message))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_float(message):# le paramètre message est dans la fonction remplissage_liste()
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Ce programme vous permet de faire la copie d'une liste que vous aurai entrer au préalable")
print("Remplissez la liste :")
liste = []
liste = remplissage_liste(liste)
copie = []
copie = copier_liste(liste)
print(f"Copie faite\nORIGINALE : {liste}   COPIE : {copie}")