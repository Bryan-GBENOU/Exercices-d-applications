"""
Le programme contient une fonction moyenne_liste(lst) qui calcule et retourne la moyenne des éléments d'une liste.
Le programme réutilise la fonction somme_liste() d'un l'exercice précédent
"""
def somme_liste(liste):
    total = 0
    for i in liste:
        total = total + i
    return total

def moyenne_liste(liste):
    return (somme_liste(liste)/len(liste))

def remplissage_liste(taille, liste):
    for i in range(taille):
        élément = récuperation_saisie_float()
        liste.append(élément)
    return liste

def récuperation_saisie_entier():
    while True:
        try:
            valeur = int(input("La valeur : "))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input("Entrez votre valeur : "))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_float():
    while True:
        try:
            valeur = float(input("La valeur : "))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Calculons la moyenne des éléments d'une liste de voir choix")
print("Entrez la taille de la liste souhaitée")
taille = récuperation_saisie_entier()
print("Remplissez la liste")
liste = []
liste = remplissage_liste(taille, liste)
print(f"La moyenne de {liste} est {moyenne_liste(liste):.5g}")
