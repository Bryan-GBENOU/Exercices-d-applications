"""
Le programme contient la fonction salaire_hebdo(heures, taux) qui calcule le salaire d'un employé :
• Les 35 premières heures sont payées normalement
• Les heures au-delà de 35 sont payées à 150%
La fonction retourne le salaire total.
"""
def salaire_hebdo(heures, taux):

    heure_supp = heures - 35
    salaire = 35 * taux + heure_supp * taux * (150/100)
    return salaire

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

print("Ce programme vous permet de connaître votre salaire hebdomdaire en \
fonction de votre taux horaire hebdomadaire et de votre rémunération à l'heure")
print("Pour se faire, entrez votre taux horaire hebdomadaire :")
heure = récuperation_saisie()
print("Entrez votre salaire horaire : ")
taux = récuperation_saisie()
print(f"Cette semaine vous avez fait {heure:.5g} heure, vous êtes payés {taux:.5g} de heure donc \
vous serez payés {salaire_hebdo(heure, taux):.5g} ")