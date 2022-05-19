# -*- coding: UTF-8 -*-
"""Les instructions de choix."""
# import
from math import sqrt
x = float(input("x ? "))
if x >= 0:
    y = sqrt(x)
    print("La racine de {:.2f} est {:.3f}".format(x, y))
else:
    print("On ne peut pas prendre la racine d'un reel negatf !")

print("\nAu revoir")
