"""
Le programme contient la fonction ecreter_liste(lst, valeur_max) qui met à 0 tous les éléments
supérieurs à valeur_max et retourne la liste modifiée
"""
def ecreter_liste(liste, valeur_max):
    i = 0
    for i in range(len(liste)):
        if liste[i] > valeur_max:
            liste[i] = 0
    return liste

def remplissage_liste(liste):
    taille = récuperation_saisie_entier("Quelle est la taille souhaitée pour votre liste ?\n")
    for i in range(taille):
        élément = récuperation_saisie_float("Entrez un élément de la liste : ")
        liste.append(élément)
    return liste

def récuperation_saisie_entier(message): #principalement utiliser pour la taille du tableau. le paramètre message est dans la fonction remplissage_liste()
    while True:
        try:
            valeur = int(input(message))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_float(message): #principalement utiliser pour les éléments du tableau. le paramètre message est dans la fonction remplissage_liste()
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Ce programme vous permet d'écrêter une liste,\
 c'est-à-dire supprimer les valeurs d'une liste supérieur à un seuil de votre choix")
print("Pour se faire, remplissez votre liste")
liste = []
liste = remplissage_liste(liste)
valeur_max = récuperation_saisie_float("Entrez la valeur maximale pour l'écrêtage :")
liste_ecreter = ecreter_liste(liste, valeur_max)
print(f"Après écrêtage par rapport à {valeur_max}, votre liste devient {liste_ecreter}")
