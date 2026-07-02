"""
Le programme permet à deux étudiants ont chacun une liste de matières de savoir :
(1) les matières communes aux deux
(2) toutes les matières au total
(3) les matières que seul l'étudiant A suit
(4) les matières que l'un ou l'autre suit mais pas les deux
Utiliser les opérations de sets pour trouver les résultats attendus
"""

def récupération_saisie_entier(message):
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

def remplissage_ensemble(ensemble):
    while True:
        element = récuperation_saisie_str("Entrez des éléments à ajouter à l'ensemble (tapez 'fin' pour arrêter) :").lower()
        if element.lower() == "fin":
            break
        ensemble.add(element)
    return ensemble

def menu():
    choix = récupération_saisie_entier("Que souhaitez-vous faire ?\n")
    while choix < 1 or choix > 5:
        print("Saisie invalide, votre choix n'est pas dans l'intervalle souhaité. Veuillez réessayer")
        choix = récupération_saisie_entier("Que souhaitez-vous faire ?\n")
    return choix

def matiere_commune (ensemble1, ensemble2):
    return (ensemble1 & ensemble2)

def matiere_totale (ensemble1, ensemble2):
    return (ensemble1 | ensemble2)

def matiere_A (ensemble1, ensemble2):
    return (ensemble1 - ensemble2)

def matiere_non_commune (ensemble1, ensemble2):
    return (ensemble1 ^ ensemble2)

print("Le programme permet à deux étudiants d'entrer chacune de leur différentes matières pour voir :")
print("1 - les matières communes aux deux")
print("2 - toutes les matières au total")
print("3 - les matières que seul l'étudiant A suit")
print("4 - les matières que l'un ou l'autre suit mais pas les deux")
print("5 - Et quittez")
print("Remplissez l'ensemble des matières du 1er étudiant :")
matiere1 = set()
matiere1 = remplissage_ensemble(matiere1)
print("Remplissez l'ensemble des matières du 2ème étudiant :")
matiere2 = set()
matiere2 = remplissage_ensemble(matiere2)
choix = menu()
while choix != 5:
    match (choix):
        case 1:
            print(f"Les matières communes aux deux étudiants sont {matiere_commune(matiere1, matiere2)}")
        case 2:
            print(f"L'ensemble de toutes les matières est {matiere_totale(matiere1, matiere2)}")
        case 3:
            print(f"Les matières que seul premier étudiant suit sont {matiere_A(matiere1, matiere2)}")
        case 4:
            print(f"Les matières que l'un ou l'autre suit mais pas les deux sont {matiere_non_commune(matiere1, matiere2)}")
        case 5:
            break
    print("Le programme permet à deux étudiants d'entrer chacune de leur différentes matières pour voir :")
    print("1 - les matières communes aux deux")
    print("2 - toutes les matières au total")
    print("3 - les matières que seul l'étudiant A suit")
    print("4 - les matières que l'un ou l'autre suit mais pas les deux")
    print("5 - Et quittez")
    choix = menu()