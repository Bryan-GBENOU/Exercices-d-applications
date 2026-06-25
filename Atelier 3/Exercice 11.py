"""
Le programme permet de calculer et afficher les 20 premiers termes de la suite de Lucas
La suite de Lucas est définie par :
• U0 = 2, U1 = 1
• U(n+2) = U(n+1) + U(n)
"""

print("La suite de Lucas est définie par :")
print("• U0 = 2, U1 = 1")
print("• U(n+2) = U(n+1) + U(n)")
u0 = 2
u1 = 1
suite = [u0, u1]
n = 2
while n < 20:
    u_n = suite[n-1] + suite[n-2]
    suite.append(u_n)
    n += 1
print("Les 20 premiers terme sont : ")
for posi, val in enumerate(suite):
    print(f"{posi} -> {val}")