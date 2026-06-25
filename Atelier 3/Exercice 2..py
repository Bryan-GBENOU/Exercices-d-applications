"""
Le programme demande un nombre entre 10 et 20 en boucle à l'utilisteur, jusqu'à ce que la réponse soit valide.
"""
import random
x = random.randint(10, 20)
print("Jouons au devinette !\nEssayez de devinez le nombre mystère caché entre 10 et 20")
while True:
    try:
        nombre = int(input("Entrez un nombre : "))
        while nombre < 10 or nombre > 20:
            print("le nombre saisie n'est pas dans l'intervalle souhaité, veuillez réessayer")
            nombre = int(input("Entrez un nombre : "))

        if nombre < x:
            print("Trop petit")
        elif nombre > x:
            print("Trop grand")
        else:
            print("Bravo")
            break
    except ValueError:
        print("Saisie invalide, veuillez réessayer")