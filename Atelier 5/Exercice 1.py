"""
Le programme contient une fonction afficher_rectangle(lignes, colonnes) qui affiche un rectangle
d'étoiles selon les dimensions passées en paramètres. Un programme principal appelle cette fonction.
"""
def afficher_rectangle(lignes, colonnes):
    for i in range(lignes):
        print("*"*colonnes)
#rajouter un intervalle pour éviter les nombre négatif
def récuperation_saisie():
    while True:
        try:
            valeur = int(input("Entrez votre valeur : "))
            while valeur <= 0:
                print("Saisie invalide, veuillez réessayer")
                valeur = int(input("Entrez votre valeur : "))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Réalisons un rectangle étoiles !")
print("Pour cela, entrez le nombre de ligne et de colonne souhaitée pour le rectangle")
print("Le nombre de ligne")
ligne = récuperation_saisie()
print("Le nombre de colonne")
colonne = récuperation_saisie()
print("On obtient donc : ")
afficher_rectangle(ligne, colonne)
