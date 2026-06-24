"""
Le programme contient une fonction volume_sphere(r) qui calcule le volume d'une sphère de rayon r.
Formule : V = (4/3) x pi x r³
"""

import math

def volume_sphere(rayon):
    return (4/3) * math.pi * rayon**3

def récuperation_saisie():
    while True:
        try:
            valeur = float(input("Entrez votre valeur : "))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input("Entrez votre valeur : "))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Calculons le volume d'une sphère !")
print("Pour se faire, entrez le rayon du cercle")
rayon = récuperation_saisie()
print(f"Le volume d'une sphère de rayon {rayon:.5g} est {volume_sphere(rayon):.5g}")