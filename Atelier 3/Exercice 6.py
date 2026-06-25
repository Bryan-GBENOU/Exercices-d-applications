"""le programme demande un entier n à l'utilisateur et affiche sa table de multiplication de 1 à 10"""
while True:
    try:
        n = int(input("Entrez votre nombre, nous afficherons sa table multiplication de 1 à 10 : "))
        while n < 1:
            print("Saisie invalide, veuillez réessayer")
            n = int(input("Entrez votre nombre, nous afficherons sa table multiplication de 1 à 10 : "))
        break
    except ValueError:
        print("Saisie invalide, veuillez réessayer")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")