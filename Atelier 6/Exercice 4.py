"""
Le programme part d'une liste de mots pour construire un dictionnaire associant chaque mot à sa longueur.
Puis un second dictionnaire ne garde que les mots de plus de 4 lettres. 
Des compréhensions de dictionnaires sont utiliser dans les deux cas
"""
def récuperation_saisie_entier(message):
    while True:
        try:
            valeur = int(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_str(message):
    while True:
        chaine = input(message)
        if chaine.isalpha():
            return chaine
        print(f"Saisie invalide, veuillez entrer votre mot en toutes lettres")

def remplissage_liste(liste):
    taille = récuperation_saisie_entier("Quelle est la taille souhaitée pour votre liste ?\n")
    for i in range(taille):
        élément = récuperation_saisie_str("Entrez un mot de la liste : ")
        liste.append(élément)
    return liste

print("Ce programme permet d'entrer une liste de mot de votre choix, ensuite il ne gardera que les mots ayant 4 lettres et plus")
liste = []
liste = remplissage_liste(liste)
dictionnaire1 = {mot : len(mot) for mot in liste}
dictionnaire2 = {mot : longueur for mot, longueur in dictionnaire1.items() if longueur > 4}
print("On a donc :")
for clé, valeur in dictionnaire2.items():
    print(f"{clé} : {valeur}")