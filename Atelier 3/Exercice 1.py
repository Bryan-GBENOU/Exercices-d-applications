"""
Le programme d'afficher le plus grand et le plus petit d'une suite d'entiers saisis par l'utilisateur.
La suite se termine quand l'utilisateur saisit 0.
Les nombres ne sont pas à conserver en mémoire.
"""
def récupérer_saisie():
    while True:
            try:
                nombre = int(input("Entrez un nombre : "))
                return nombre
            except ValueError:
                print("Saisie invalide, veuillez réessayer")

print("Entrez une suite de nombres entiers, on vous dira le plus grand et le plus petit !")
print("Arrêtez la saisie avec zéro : 0")
while True:
    try:
        nombre = int(input("Entrez un nombre : "))
        break
    except ValueError:
        print("Saisie invalide, veuillez réessayer")
#de la ligne 8 à 14 pour récupérer la 1ère saisie de l'utilisateur
if nombre == 0:
    print("On s'arrête là alors, pas de maximum ni de minimum") #comme ça si après la 1ère saisie l'utilisateur met 0, on s'arrête
else:
    maxi = nombre
    mini = nombre
    while True:
        nombre = récupérer_saisie()
        if nombre == 0:
            print(f"Le maximum est {maxi} et le minimum est {mini}")
            break
        if nombre > maxi:
            maxi = nombre
        if nombre < mini:
            mini = nombre
#j'ai utilisé 3 if pour qu'il s'éxecute différemment, à part l'un de l'autre