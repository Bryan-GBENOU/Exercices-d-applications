"""
Le programme permet de saisir une phrase au clavier.
Il compte ensuite le nombre d'occurrences de chaque mot (sans tenir compte de la casse).
Enfin, le programme afficher les 3 mots les plus fréquents avec leur nombre d'apparitions. 
Ne pas utiliser Counter : construire le dictionnaire manuellement.
"""
phrase = input("Entrez une phrase de votre choix :\n").lower()
liste_mot = phrase.split()
compteur_occurence = {}
for mot in liste_mot:
    if mot in compteur_occurence:
        compteur_occurence[mot] += 1
    else:
        compteur_occurence[mot] = 1
compteur_occurence_ordonne = sorted(compteur_occurence.items(), key=lambda x: x[1], reverse=True)
print(compteur_occurence_ordonne[:3])