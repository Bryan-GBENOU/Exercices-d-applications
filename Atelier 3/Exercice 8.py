"""Le programme demande deux entiers et calcule leur Plus Grand Commun Diviseur (PGCD) en utilisant l'algorithme d'Euclide."""

def récupérer_saisie(message):
    while True:
            try:
                nombre = int(input(message))
                return nombre
            except ValueError:
                print("Saisie invalide, veuillez réessayer")

print("Calculons le PGCD de deux nombres !")
a = récupérer_saisie("Entrez votre premier nombre : ")
b = récupérer_saisie("Entrez votre second nombre : ")

c = abs(a)
d = abs(b)
#Algorithme d'Euclide :
#Tant que b != 0 : a, b = b, a % b
#Si b == 0 alors PGCD(a, b) = a 
while d != 0:
    c, d = d, c % d
print(f"PGCD({a}, {b}) =  {c}")
# uutilisation du module math
import math
print(f"PGCD({a}, {b}) =  {math.gcd(a, b)}")