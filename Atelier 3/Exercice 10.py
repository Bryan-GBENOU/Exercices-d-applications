"""
Le programme calcule x^n par multiplications successives, sans utiliser l'opérateur ** ni la fonction math.pow()
"""
def récupérer_saisie(message):
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Entrez 2 nombres, la base et l'exposant, et on vous donnera le résultat")
x = récupérer_saisie("Entrez la base : ")
n = récupérer_saisie("Entrez l'exposant : ")
résultat = 1
i = 0
if n >= 0:
    while i < n:
        résultat = résultat*x
        i += 1
    print(f"{x:.5g} exposant {n:.5g} = {résultat:.5g}")
elif n < 0:
    while i < abs(n):
        résultat = résultat*x
        i += 1
    résultat = résultat**-1
    print(f"{x:.5g} exposant {n:.5g} = {résultat:.5g}")