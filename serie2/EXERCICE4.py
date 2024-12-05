class Personne:
    def __init__(self,nom, prenom, age):
        self.nom=nom
        self.prenom=prenom
        self.age=age

    def se_presenter(self):
        print("Bonjour je m'appelle : {} {} et j'ai : {}".format(self.nom, self.prenom, self.age))

    
class Etudiant(Personne):
    def __init__(self,nom, prenom, age, matricule):
        super().__init__(nom, prenom,age)
        self.matricule=matricule
    def etudier(self):
        print("L'etudiant {} {} a le matricule: {}".format(self.nom, self.prenom, self.matricule))

# Exemple d'utilisation
Etu1=Etudiant("hilal","ahmed",23,"D133455550")
Etu2=Etudiant("salim","sara",25,"D145678950")

Etu1.se_presenter()
Etu2.etudier()