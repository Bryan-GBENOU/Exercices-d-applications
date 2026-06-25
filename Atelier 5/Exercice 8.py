"""
Le programme contient la fonction volume_cone(r, h) qui calcule le volume d'un cône de révolution.
Formule : V = (1/3) x pi x r² x h
"""
import math
def volume_cone(rayon, hauteur):
    return ((1/3) * math.pi * (rayon**2) * hauteur)

def récuperation_saisie():
    while True:
        try:
            valeur = float(input("La valeur : "))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input("Entrez votre valeur : "))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Calculons le volume d'un cône de révolution !")
print("Pour ce faire, entrez le rayon et la hauteur du cône")
print("Le rayon ")
rayon = récuperation_saisie()
print("La hauteur ")
hauteur = récuperation_saisie()
print(f"Le volume d'un cône de hauteur {hauteur:.5g} et de rayon {rayon:.5g} est {volume_cone(rayon, hauteur):.5g}")
