"""
Le programme contient une fonction moyenne(a, b, c) qui retourne la moyenne de trois réels.
Le programme teste la fonction avec plusieurs appels.
"""
def moyenne(a, b, c):
    tuple_réel = (a, b, c)
    return(sum(tuple_réel)/len(tuple_réel))

def récuperation_saisie():
    while True:
        try:
            valeur = float(input("La valeur : "))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Calculons la moyenne de trois réels de votre choix")
print("Entrez le premier réel")
reel1 = récuperation_saisie()
print("Entrez le deuxième réel")
reel2 = récuperation_saisie()
print("Entrez le troisième réel")
reel3 = récuperation_saisie()
print(f"La moyenne de {reel1:.5g}, {reel2:.5g} et {reel3:.5g} est {moyenne(reel1, reel2, reel3):.5g}")
