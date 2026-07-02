"""
Le programme contient un dictionnaire représentant un étudiant (nom, prénom, age, note moyenne).
Le programme affiche chaque champ sous la forme clé : valeur et 
permet d'accéder ensuite à un champ inexistant ("email") avec .get() et une valeur par défaut.
"""

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

def récuperation_saisie_str(message, clé):
    while True:
        chaine = input(message)
        while not chaine.isalpha():
            print(f"Saisie invalide, veuillez entrer votre {clé} en toutes lettres")
            chaine = input(message)
        return chaine

étudiant = {
    "nom" : None,
    "prénom" : None,
    "age" : None,
    "note moyenne" : None
}

print("Ce programme vous permet de stockers des renseignements vous concernant")
print("Entrez les informations suivants")
for clé in étudiant:
    if clé in ["nom", "prénom"]:
        étudiant[clé] = récuperation_saisie_str(f"Entrez votre {clé} : ", clé)

étudiant["age"] = récupération_saisie_entier("Entrez votre age : ")
while étudiant["age"] <= 0 or étudiant["age"] >= 100:
    print("Saisie invalide, veuillez réessayer")
    étudiant["age"] = récupération_saisie_entier("Entrez votre age : ")

étudiant["note moyenne"] = récupération_saisie_float("Entrez votre moyenne : ")
while étudiant["note moyenne"] < 0 or étudiant["note moyenne"] > 20:
    print("Saisie invalide, la moyenne est sur 20. Veuillez donc réessayer")
    étudiant["note moyenne"] = récupération_saisie_float("Entrez votre moyenne : ")

print("Avez-vous renseigner votre adresse mail ?\nVérifions ... ")
print({étudiant.get("email", "Inexistant")})
for clé, valeur in étudiant.items():
    print(f"{clé} : {valeur} |",end=' ')