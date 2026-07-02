"""
Le programme part d'un dictionnaire de capitales {"France": "Paris", "Bénin": "Cotonou", "Japon": "Tokyo"}.
Il permet d'afficher : (1) uniquement les clés, (2) uniquement les valeurs, (3) paires clé-valeur formatées.
"""

def menu():
    print("1 - Afficher uniquement les clés")
    print("2 - Afficher uniquement les valeurs")
    print("3 - Afficher les paires clé-valeur formatées")
    print("4 - Quittez")
    choix = récupération_saisie_entier("Que souhaitez-vous faire ?\n")
    while choix < 1 or choix > 4:
        print("Saisie invalide, votre choix n'est pas dans l'intervalle souhaité. Veuillez réessayer")
        choix = récupération_saisie_entier("Que souhaitez-vous faire ?\n")
    return choix

def récupération_saisie_entier(message):
    while True:
        try:
            valeur = int(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récupération_saisie_float(message):
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

capitales = {
    "France": "Paris",
    "Bénin": "Cotonou",
    "Japon": "Tokyo"
}

print("Ce programme vous permet soit uniquement les pays, soit uniquement les capitales, soit les couples Pays-Capitale")
choix = menu()
while choix != 4:
    match(choix):
        case 1:
            for pays in capitales:
                print(f"{pays}")
        case 2:
            for capitale in capitales.values():
                print(f"{capitale}")
        case 3:
            for pays, capitale in capitales.items():
                print(f"{pays} : {capitale}")
        case 4:
            break
    choix = menu()