"""
Le programme pars de deux dictionnaires de notes partielles pour les mêmes étudiants (semestre 1 et semestre 2).
Il les fusionne en calculant la moyenne des deux semestres pour chaque étudiant.
Le programme affiche enfin un tableau récapitulatif trié par moyenne décroissante
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

def récupération_saisie_float(message):
    while True:
        try:
            valeur = float(input(message))
            while valeur <= 0 or valeur > 20:
                print("Saisie invalide, veuillez réessayer")
                valeur = float(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def récuperation_saisie_str(message):
    while True:
        chaine = input(message)
        while not chaine.isalpha():
            print(f"Saisie invalide, veuillez entrer le nom de l'élève en toutes lettres")
            chaine = input(message)
        return chaine

def remplissage_dictionnaire(dictionnaire1, dictionnaire2):
    n = récupération_saisie_entier("De combien d'etudiant s'agit-il ?\n")
    for i in range(n):
        nom = récuperation_saisie_str("Entrez le nom des étudiants : ")
        dictionnaire1[nom] = récupération_saisie_float("Entrez ça note au premier semestre : ")
        dictionnaire2[nom] = récupération_saisie_float("Entrez sa note au second semestre : ")
    return dictionnaire1, dictionnaire2


semestre1 = {}
semestre2 = {}
print("Ce programme...")
print("Entrez le nom de l'étudiant puis sa note au premier semestre et enfin sa note au second semestre")
semestre1, semestre2 = remplissage_dictionnaire(semestre1, semestre2)
etudiant_total = set(semestre1.keys()) |  set(semestre2.keys())
semestre1_2 = {}
for etudiant in etudiant_total:
    note_s1 = semestre1.get(etudiant, 0)
    note_s2 = semestre2.get(etudiant, 0)
    moyenne = (note_s1 + note_s2) / 2
    semestre1_2[etudiant] = moyenne
liste = sorted(semestre1_2.items(), key= lambda x : x[1], reverse= True)
print(liste)