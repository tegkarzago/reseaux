# -*- coding: UTF-8 -*-
"""Les instructions de choix (2)
Trouver le minimum de deux nombres"""
# fichier : cours2_10.py
# auteur : Bob Cordeau
# programme principal
print("Donnez deux valeurs entieres :")
x = int(input("n1 = "))
y = int(input("n2 = "))
# ecriture classique :
if x < y:
    plus_petit = x
else:
    plus_petit = y
# ecriture compacte :
plus_petit = x if x < y else y
print("\nLa plus petite des deux est", plus_petit)
print("\nAu revoir Tonton TEG")
