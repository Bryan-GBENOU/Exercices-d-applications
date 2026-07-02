"""
Implémenter un mini-annuaire de contacts en ligne de commande.
Chaque contact est un dictionnaire imbriqué {"nom": ..., "tel": ..., "email": ..., "ville": ...}.
Proposer un menu : (A)jouter, (R)echercher par nom, (S)upprimer, (L)ister par ville, (Q)uitter.
La recherche doit être insensible à la casse et aux espaces
"""

def récupération_saisie_entier(message):
    while True:
        try:
            valeur = int(input(message))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_str(message):
    while True:
        chaine = input(message).strip().lower()
        if chaine and all(c.isalpha() or c.isspace() for c in chaine):
            return chaine
        print("Saisie invalide, veuillez écrire en toutes lettres")

def saisir_email(message):
    while True:
        email = input(message)
        if "@" in email and "." in email.split("@")[-1]:
            return email
        print("Email invalide, réessayez.")

def saisir_num_tel(message):
    tel = input(message).strip()
    while not (tel.isdigit() and len(tel) >= 8):
        print("Numéro invalide, veuillez réessayer avec le format : +XXX XXXXXXXX")
        tel = input(message).strip()
    return tel

def ajouter_contact(dictionnaire):
    nom = récuperation_saisie_str("Entrez le nom de votre conctact : ")
    dictionnaire[nom] = {}
    tel = saisir_num_tel(f"Entrez le numéro de téléphone de {nom}: ")
    dictionnaire[nom]["téléphone"] = tel
    email = saisir_email(f"Entrez l'adresse email de {nom}: ")
    dictionnaire[nom]["E-mail"] = email
    adresse = récuperation_saisie_str(f"Entrez l'adresse (la ville de résidence) : {nom}")
    dictionnaire[nom]["Adresse"] = adresse

def recherche_par_nom(dictionnaire, clé):
    return dictionnaire.get(clé, "Inexistant")

def supprimer(dictionnaire, clé):
    if clé in dictionnaire:
        del dictionnaire[clé]
        print("Suppression faite")
    else:
        print("Ce contact n'existe pas dans l'annuaire")

def liste_par_ville(dictionnaire):
    ville_individu = {}
    for individu, information in dictionnaire.items():
        adresse = information["Adresse"]
        ville_individu.setdefault(adresse, []).append(individu)
    return ville_individu

def menu():
    print("(A)jouter")
    print("(R)echercher par nom")
    print("(S)upprimer")
    print("(L)ister par ville")
    print("(Q)uitter")
    choix = récuperation_saisie_str("Que voulez-vous faire ?\n").strip().lower()
    while choix not in ['A', 'R', 'S', 'L', 'Q', 'a', 'r', 's', 'l', 'q']:
        print("Saisie invalide, veuillez réessyer")
        choix = récuperation_saisie_str("Que voulez-vous faire ?\n").strip().lower()
    return choix

annuaire = {}
print("Ce programme...")
choix = menu()
while choix in ['A', 'R', 'S', 'L', 'Q', 'a', 'r', 's', 'l', 'q']:
    match(choix):
        case "a":
            ajouter_contact(annuaire)
            for individu, infos in annuaire.items():
                print(f"{individu} : {infos}")
        case "r":
            nom = récuperation_saisie_str("Entrez le nom du conctact que vous recherchez : ")
            print(f"{nom} : {recherche_par_nom(annuaire, nom)}")
        case "s":
            nom = récuperation_saisie_str("Entrez le nom du conctact que vous voulez supprimer : ")
            supprimer(annuaire, nom)
        case "l":
            print(f"{liste_par_ville(annuaire)}")
        case "q":
            break
    choix = menu()