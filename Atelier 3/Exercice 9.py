"""
Le programme choisit un nombre entre 1 et 100
L'utilisateur a 10 tentatives pour le trouver.
À chaque essai : afficher "Plus grand", "Plus petit" ou "Gagné !
"""
import random
print("Jouons au devinette !\nEssayez de devinez le nombre mystère caché entre 1 et 100 en 10 tentatives")
x = random.randint(1, 100)
while True:
    try:
        nombre = int(input("Entrez un nombre : "))
        while nombre < 1 or nombre > 100:
            print("le nombre saisie n'est pas dans l'intervalle souhaité, veuillez réessayer")
            nombre = int(input("Entrez un nombre : "))
        break
    except ValueError:
        print("Saisie invalide, veuillez réessayer")

for i in range(10):
    try :
        if i == 5:
            print("Il vous reste 5 essais")
        elif i == 9:
            print("Il ne vous qu'un essai")
        
        if nombre < x:
            print("Trop petit")
            nombre = int(input("Entrez un nombre : "))
            while nombre < 1 or nombre > 100:
                print("le nombre saisie n'est pas dans l'intervalle souhaité, veuillez réessayer")
        elif nombre > x:
            print("Trop grand")
            nombre = int(input("Entrez un nombre : "))
            while nombre < 1 or nombre > 100:
                print("le nombre saisie n'est pas dans l'intervalle souhaité, veuillez réessayer")
        else:
            print("Bravo")
            break
    except ValueError:
        print("Erreur de saisie, veuillez réessayer")
        
    