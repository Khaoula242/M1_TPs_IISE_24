class Employe():
    def __init__(self,nom,prenom,salaire):
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.listEmp=[]
    
    def ajouterEmp(self,Emp):
        if Emp not in self.listEmp:
            self.listEmp.append(Emp)
        else:
            print("Cet employé est déja dans la liste") # Message si l'employé est déjà ajouté

    def Afficher_list_Employés(self):
        print("__________________________Liste des employés_____________________________")
        for employe in self.listEmp:
            print("Nom:\t {}\nPrenom:\t {}\nSalaire:{}\n".format(employe.nom,employe.prenom,employe.salaire))


if __name__ =="__main__":

    # Création d'un manager
    Manager1=Manager("karim","salah",10000)

    # Création de deux employés
    Employe1=Employe("alami","ranya",7000)
    Employe2=Employe("sayk","fouad",6000)

    # Ajout des employés au manager
    Manager1.ajouterEmp(Employe1)
    Manager1.ajouterEmp(Employe2)
    Manager1.ajouterEmp(Employe1)    # Tentative d'ajout d'un employé déjà présent


    # Affichage de la liste des employés supervisés par le manager
    Manager1.Afficher_list_Employés()





