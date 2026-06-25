"""Le programme calcule la somme des n premiers termes de la série harmonique : S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n"""
print("Le programme te permet de calculer la somme des n premiers termes de la série harmonique")
print("La série harmonique est sous la forme : S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n")
while True:
    try:
        n = int(input("Entrez votre nombre, nous calculerons la somme : "))
        while n < 1:
            print("Saisie invalide, veuillez réessayer")
            n = int(input("Entrez votre nombre, nous calculerons la somme : "))
        break
    except ValueError:
        print("Saisie invalide, veuillez réessayer")
somme = 0
for i in range(1, n+1):
    somme = somme + i**-1
print(f"La sommme de la série harmique de 1 à 1/{n} est {somme:.5g}")