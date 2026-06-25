"""Le programme demande un entier n à l'utilisateur et calcule n! (la factorielle)"""
print("Calculons le factorielle d'un nombre de votre choix !")
while True:
    try:
        n = int(input("Entrez votre nombre : "))
        while n < 0:
            print("Saisie invalide, veuillez réessayer")
            n = int(input("Entrez votre nombre : "))
        break
    except ValueError:
        print("Saisie invalide, veuillez réessayer")
produit = 1
for i in range(1, n+1):
    if n == 0:
        produit = 1
        break
    produit = produit*i
print(f"Le factorielle de {n} est {produit}")