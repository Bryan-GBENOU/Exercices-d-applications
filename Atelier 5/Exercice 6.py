"""
Le programme contient une fonction resoudre_eq2(a, b, c) qui prend les coefficients d'une équation du
2nd degré et retourne les racines réelles s'il y en a.
La fonction retourne un tuple selon les cas
"""
import math
import cmath
def resoudre_eq2(a, b, c):
    #la fonction ne retourne que des tuples
        if a == 0:
            if b == 0:
                return()
            elif c == 0:
                return"L'équation admet une infinité de solution"
            else:
                x = (-c/b,)
                return x

        else:
            delta = b**2 - 4*a*c
            if delta == 0:
                x = (-b/(2*a),)
                return x

            elif delta > 0:
                x1 = (-b+math.sqrt(delta))/(2*a)
                x2 = (-b-math.sqrt(delta))/(2*a)
                return (x1, x2)

            else:
                x1 = (-b+cmath.sqrt(delta))/(2*a)
                x2 = (-b-cmath.sqrt(delta))/(2*a)
                return (x1, x2)

def récuperation_saisie():
    while True:
        try:
            valeur = float(input("Entrez votre valeur : "))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("RESOLVONS UNE EQUATION DE DEGRE 2 !")
print("Elles sont sous la forme de Ax² + Bx + C = 0")
print("Entrez la constante A :")
A = récuperation_saisie()
print("Entrez la constante B :")
B = récuperation_saisie()
print("Entrez la constante C :")
C = récuperation_saisie()
print(resoudre_eq2(A, B, C))
