"""
Le programme contient une fonction trier_liste(lst) qui trie une liste par ordre croissant sans utiliser
sort(). Il procède par implémentation au tri par sélection c'est-à-dire qu'à
chaque tour, le minimum est placé en tête.
Schéma mentale (fait par IA) : 
Imagine des billes
Tu as une rangée de billes avec des nombres dessus :
[5, 2, 8, 1]
Ton but : ranger les billes du plus petit au plus grand.
 Étape par étape
On cherche la plus petite bille dans toute la rangée.
Ici, c'est 1.
→ On la met tout au début.
Résultat : [1, 2, 8, 5].
On recommence, mais cette fois on ne regarde plus que les billes après la première (car elle est déjà bien placée).
Dans [2, 8, 5], la plus petite est 2.
→ On la laisse où elle est.
Résultat : [1, 2, 8, 5].
Troisième tour : on regarde [8, 5].
La plus petite est 5.
→ On échange 8 et 5.
Résultat : [1, 2, 5, 8].
Dernier tour : il ne reste qu'une bille (8), donc c'est fini.
 La liste est triée : [1, 2, 5, 8].
"""
def trier_liste(liste):
    n = len(liste) # on va travailler avec la taille
    for i in range(n): # 1ère boucle pour que la vérification des modification de la seconde soit faite
        indice_minimum = i # on suppose que indice du minimum est i (le 1er nombre à la première itération par exemple)
        for j in range(i + 1, n): # la seconde boucle pour que le travaille soit réellement fait. Elle commence a i+1 car on suppose que le nombre à l'indice i est réellemnt le plus petit
            if liste[j] < liste[indice_minimum]: # si par exemple le chiffre de la 2ème case est inférieur à celui de la 1ère, alors :
                indice_minimum = j # l'indice du minimum devient par exemple la 2ème case si la conditon di if est vérifiée
        liste[i], liste[indice_minimum] = liste[indice_minimum], liste[i] # le supposé minimum devient le minimum réel (liste[i] = liste[indice_minimum]) et l'autre devient la case d'après
    return liste

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

print("Ce programme vous permet de trier dans l'ordre croissant une liste de votre choix")
print("Pour ce faire, remplissez votre liste")
liste = []
liste = remplissage_liste(liste)
liste = trier_liste(liste)
print(f"Après tri, votre liste devient {liste}")
