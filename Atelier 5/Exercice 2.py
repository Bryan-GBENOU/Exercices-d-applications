"""
Le programme contient une fonction km_en_miles(km) qui convertit des kilomètres en miles (1 mile = 1,609 km).
La fonction retourne le résultat. Un programme principal teste la fonction
"""
def km_en_miles(distance_en_km):
    return distance_en_km * (1.609**-1)

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

print("Ce programme vous permet de convertir des distances en kilomètre en miles")
print("Pour cela, entrez votre valeur")
distance = récuperation_saisie()
print(f"{distance:.5g} kilomètre font {km_en_miles(distance):.5g}")
