
class Personne:
    def affiche(self):
        return "l'etudiant:{} {} est né le {} à {}  et à pour matricule {} est de sexe {} ".format(self.prenom,self.nom,self.date,self.lieu,self.matricule,self.sexe)

if __name__ == "__main__":
    
    etudiant = Personne()
    etudiant.prenom = input("quel est votre prenom ")
    etudiant.nom = input("quel est votre nom ")
    etudiant.date = input("votre date de naissance ")
    etudiant.lieu = input("lieu de naissance ")
    etudiant.matricule = input("votre matricule ")
    etudiant.sexe = input("votre genre ")
    aff = etudiant.affiche()
    print(aff)


