class Personne:
    def __init__(self,nom, prenom, age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.amis = []

    def se_presenter(self):
        print("Bonjour je m'appelle : {} {} et j'ai : {}".format(self.nom, self.prenom, self.age))

    def ajouter_ami(self, ami):
        if ami not in self.amis:
            self.amis.append(ami)
        else:
            print("{} est déjà dans la liste d'amis de {}.".format(ami,self.nom))

    def afficher_amis(self):
        if not self.amis:
            print("{} n'a pas encore d'amis.".format(self.nom))
        else:
            print("Liste des amis de {} :".format(self.nom))
            for ami in self.amis:
                print("\t- {}".format(ami))

# Exemple d'utilisation
personne = Personne("Dupont", "Alice", 30)  
personne.se_presenter()  
personne.ajouter_ami("Bob")
personne.ajouter_ami("Charlie")
personne.ajouter_ami("Bob")  # Tester un ami déjà ajouté
personne.afficher_amis()
