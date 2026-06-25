"""
Dans le programme, on représente les nombres complexes sous forme de tuple (partie_reelle, partie_imaginaire).
Le programme contient la fonction somme_complexe(z1, z2) qui retourne la somme de deux nombres complexes.
Le programme principal permet de :
• Saisir les parties réelles et imaginaires de deux nombres
• Calculer la somme (via la fonction)
• Affiche le résultat sous la forme a + bi
"""
def somme_complexe(complexe1, complexe2):
    return(complexe1[0] + complexe2[0], complexe1[1] + complexe2[1])

def récuperation_saisie_float(message):
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

def affichage_tuple_to_complex(tuple):
    if tuple[1] < 0:
        return f"{tuple[0]} - i{abs(tuple[1])}"
    else:
        return f"{tuple[0]} + i{tuple[1]}"

print("Vous pouvez calculer la somme de deux nombres complexes grâce à ce programme")
print("Entrez vos nombres complexes")
#complex1 = a + ib  complex2 = c + id
réel1 = récuperation_saisie_float("Entrez la partie réelle de votre 1er nombre complexe : ")
imaginaire1 = récuperation_saisie_float("Entrez la partie imaginaire le de votre 1er nombre complexe : ")
réel2 = récuperation_saisie_float("Entrez la partie réelle de votre 2ème nombre complexe : ")
imaginaire2 = récuperation_saisie_float("Entrez la partie imaginaire le de votre 2ème nombre complexe : ")
complex1 = (réel1, imaginaire1)
complex2 = (réel2, imaginaire2)
print(f"({affichage_tuple_to_complex(complex1)}) + ({affichage_tuple_to_complex(complex2)}) = ({affichage_tuple_to_complex(somme_complexe(complex1, complex2))})")
