
class Personne:
    def affiche(self):
        return "l'etudiant:{} est né le{}à{}et à pour matricule {} est de sexe{} ".format(self.prenom,self.nom,self.date,self.lieu,self.matricule,self.sexe)
    def ___init__(self,prenom,nom,age,date,lieu,matricule,sexe):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        sel.date = date
        self.lieu = lieu
        self.matricule = matricule
        self.sexe = sexe
        
        if __name__ == "__main__":
            
            etudiant = Personne("Teg","terance","01/10/1990","dakar","3306","masculin")
            aff = etudiant.affiche()
            print(aff)


