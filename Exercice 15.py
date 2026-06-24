"""
Le programme contient une fonction plus_grand(lst) qui retourne la valeur du plus grand élément d'une liste sans utiliser max()
"""
def plus_grand(liste):
    maximum = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > maximum:
            maximum = liste[i]
    return maximum

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

print("Entrez une liste de nombre et on vous dira qu'elle est le maximum de celle-ci !")
liste = []
liste = remplissage_liste(liste)
print(f"Le maximum de la liste {liste} est {plus_grand(liste):.5g}")