"""
Le programme contient une fonction fahrenheit_en_celsius(f) qui convertit des degrés Fahrenheit en
Celsius.
Formule : C = (F - 32) x 5/9
le programme principal pour la tester.
"""
def fahrenheit_en_celsius(degré_Fahrenheit):
    return (degré_Fahrenheit - 32) * 5/9

def récuperation_saisie():
    while True:
        try:
            valeur = float(input("Entrez votre valeur : "))
            return valeur
        except ValueError:
            print("Saisie invalide, veuillez réessayer")

print("Ce programme vous permet de convertir les degrés Fahrenheit en degrés Celsius")
print("Pour cela, entrez la température en degré Fahrenheit")
température = récuperation_saisie()
print(f"{température:.5g}°F font {fahrenheit_en_celsius(température):.5g}°C")