"""
Le programme contient fonction premier_negatif(lst) qui retourne l'indice du premier élément
strictement négatif parmi les éléments d'une liste.
Si aucun élément n'est négatif, elle retourne -1
"""
def premier_negatif(liste):
    i = 0
    for i in range(len(liste)):
        if liste[i] < 0:
            return i
    return -1

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

print("Ce programme vous permet d'obtenir l'indice de la première valeur négative de votre liste")
print("ATTENTION !\nSi votre liste ne contient pas d'élément négatif vous aurez affiché -1")
print("Pour ce faire, remplissez votre liste")
liste = []
liste = remplissage_liste(liste)
indice_1er_nombre_négatif = premier_negatif(liste)
if indice_1er_nombre_négatif == -1:
    print(f"Votre liste ne contient d'élément négatif : {indice_1er_nombre_négatif}")
else:
    print(f"Le 1er élément négatif de votre liste est à l'indice : {indice_1er_nombre_négatif}")