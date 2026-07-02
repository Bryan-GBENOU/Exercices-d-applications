"""
Le programme contient la fonction supprimer_doublons(liste) qui renvoie une nouvelle liste sans doublons, en préservant l'ordre d'apparition des éléments.
Le programme doit marcher avec une liste d'entiers et une liste de chaînes.
"""

def supprimer_doublons(liste):
    vus = set()
    liste_finale = []
    for i in liste:
        if i not in vus:
            vus.add(i)
            liste_finale.append(i)
    return liste_finale

def récuperation_saisie_entier(message):
    while True:
        try:
            valeur = int(input(message))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_float(message):
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_str(message):
    while True:
        chaine = input(message)
        if chaine.isalpha():
            return chaine
        print(f"Saisie invalide, veuillez entrer votre mot en toutes lettres")

def remplissage_liste(liste):
    taille = récuperation_saisie_entier("Quelle est la taille souhaitée pour votre liste ?\n")
    choix  = menu()
    if choix == 1:
        for i in range(taille):
            élément = récuperation_saisie_float("Entrez un élément de la liste : ")
            liste.append(élément)
        return liste
    elif choix == 2:
        for i in range(taille):
            élément = récuperation_saisie_str("Entrez un élément de la liste : ")
            liste.append(élément)
        return liste

def menu():
    print("Que voulez-vous que votre liste contienne ?")
    print("1 - uniquement des nombres")
    print("2 - uniquement des mots")
    choix = récuperation_saisie_entier("Faites votre choix : ")
    while choix < 1 or choix > 2:
        print("Saisie invalide, votre choix n'est pas dans l'intervalle souhaité. Veuillez réessayer")
        choix = récuperation_saisie_entier("Que souhaitez-vous faire ?\n")
    return choix

print("Ce programme vous permet de supprimer les doublons d'une liste de votre choix")
print("Remplissez votre liste")
liste = []
liste = remplissage_liste(liste)
print(f"Ainsi, on a {supprimer_doublons(liste)}")