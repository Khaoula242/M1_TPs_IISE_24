class CompteBancaire:
    def __init__(self,titulaire,solde):
       self.titulaire=titulaire
       self.solde=solde
    def deposer(self,montant):
       self.solde+=montant
    def retirer(self,montant):
       if self.solde<montant:
          print("----------Votre solde est insuffisant----------")
       else:
          self.solde-=montant
    def afficher_solde(self):
       print("----------Votre solde actuel est :{}----------".format(self.solde))
    

# Exemple d'utilisation
Cmp1=CompteBancaire("client1",20000)
Cmp2=CompteBancaire("client2",33000)

Cmp1.afficher_solde()
Cmp2.afficher_solde()

Cmp2.retirer(1000)
Cmp1.retirer(30000)
Cmp2.afficher_solde()
