"""
Le programme contient la fonction indice_plus_grand(lst) qui retourne l'indice du plus grand élément
d'une liste. En cas d'ex-æquo, retourner l'indice du premier
"""
def indice_plus_grand(liste):
    maximum = liste[0]
    indice_max = 0
    for indice, valeur in enumerate(liste):
        if valeur > maximum:
            maximum = valeur
            indice_max = indice
    return indice_max

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

print("Ce programme vous permet de connaître l'indice du nombre le plus grand d'un liste de votre choix")
print("Pour se faire, remplissez votre liste")
liste = []
liste = remplissage_liste(liste)
print(f"Le plus grand élément de {liste} est à l'indice {indice_plus_grand(liste):.5g}")