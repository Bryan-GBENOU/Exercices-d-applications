"""
Le programme part d'un dictionnaire de stock de fruits {"pommes": 10, "bananes": 5, "oranges": 8}.
L'utilisateur peut ajouter un nouveau produit, modifier la quantité d'un existant, supprimer un produit avec del, puis afficher le stock final.
"""
def menu():
    print("Entrez un chiffre entre 1 et 4 pour éxécuter la tâche correspondante")
    print("1 - Ajouter un nouveau produit")
    print("2 - Modifier la quantité d'un produit existant")
    print("3 - Supprimer un produit")
    print("4 - Afficher le stock entier")
    print("5 - Quitter")
    choix = récupération_saisie_entier("Que souhaitez-vous faire ?\n")
    while choix < 1 or choix > 5:
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

def récuperation_saisie_str(message, clé = "fruit"):
    while True:
        chaine = input(message)
        while not chaine.isalpha():
            print(f"Saisie invalide, veuillez entrer votre {clé} en toutes lettres")
            chaine = input(message)
        return chaine

def supprimer_produit(clé, dictionnaire_stock):
    del dictionnaire_stock[clé]

def affichage_stock(dictionnaire_stock):
    for fruit, nombreDeFruit in dictionnaire_stock.items():
        print(f"{fruit} : {nombreDeFruit}")

stock_fruit = {
    "pommes" : 10,
    "bananes" : 5,
    "oranges" : 8
}
print("BIENVENUE DANS VOTRE GESTIONNAIRE DE STOCK")
print("Le stock actuellement :")
for fruit, nombreDeFruit in stock_fruit.items():
    print(f"{fruit} : {nombreDeFruit}")
choix = menu()
while choix != 5:
    match (choix):
        case 1:
            clé_sup = récuperation_saisie_str("Veuillez entrez le fruit à ajouter au stock : ").lower() #clé_sup = clé supplémentaire
            stock_fruit[clé_sup] = récupération_saisie_entier("Combien il y en a t'il en stock ?\n")
            while stock_fruit[clé_sup] < 0:
                print("Saisie invalide, veuillez réessayer")
                stock_fruit[clé_sup] = récupération_saisie_entier("Combien il y en a t'il en stock ?\n")
        case 2:
            clé_modif = récuperation_saisie_str("Vous voulez modifier l'état de stock de quel fruit ?\n").lower() #clé_modif = clé à modifier
            validité = stock_fruit.get(clé_modif, "absent")
            if validité == "absent":
                print(f"{clé_modif} n'est actuellement pas en stock, vous ne pouvez donc pas modifier son stock.\nVeuillez l'ajouter grâce à la commande dédiée.")
            else:
                stock_fruit[clé_modif] = récupération_saisie_entier(f"Le stock de {clé_modif} est maintenant : ")
                while stock_fruit[clé_modif] < 0:
                    print("Saisie invalide, veuillez réessayer")
                    stock_fruit[clé_modif] = récupération_saisie_entier(f"Le stock de {clé_modif} est maintenant : ")
        case 3:
            clé_suppr = récuperation_saisie_str("Veuillez entrer le fruit à supprimer : ").lower() #clé_suppr = clé à supprimer
            if clé_suppr in stock_fruit:
                supprimer_produit(clé_suppr, stock_fruit)
                print("Suppression faite")
            else:
                print(f"{clé_suppr} n'est actuellement pas en stock, vous ne pouvez donc pas modifier son stock.\nVeuillez l'ajouter grâce à la commande dédiée.")
        case 4:
            affichage_stock(stock_fruit)
        case 5:
            break
    choix = menu()