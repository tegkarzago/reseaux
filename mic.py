# -*- coding: UTF-8 -*-
mot_de_passe = ""

while not mot_de_passe == "TEG":
	mot_de_passe = input("quel est votre mot de passe ")

nom = input("quel est votre nom ")
age = input("quel est votre age ")
age_prochain = int(age) + 1

print("Mot de passe correct, vous avez accèes au compte")

print("\nvous vous appelez : " + nom )
print("\nvous avez : " + age + str(age) + " ans")
print("\nl'an prochain vous aurez : " + str(age_prochain) + " ans")
print("\nSVP !!! la prochaine fois donnez votre vrai nom de famille sinon je vais vous tuer OK ?")
