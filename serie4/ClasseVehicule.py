# Classe de base Vehicule

# Classe Moteur
class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur
    def afficher_moteur(self):
        print('Puissance: {}\nType_Moteur: {}'.format(self.puissance,self.type_moteur))

class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        print('Marque: {}\nModele: {}\nAnnee: {}'.format(self.marque,self.modele,self.annee))

# Classe Voiture héritant de Vehicule et Moteur
class Voiture(Moteur,Vehicule):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places
    def afficher_infos(self):
        super().afficher_info()  #pourquoi self ne fonctionne pas ici
        self.afficher_moteur()
        print("Nombre de places: {}".format(self.nombre_de_places))

# Classe Moto héritant de Vehicule et Moteur
class Moto(Moteur,Vehicule):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print("Type de moto: {}".format(self.type_moto))

# Création d'une instance de Voiture
voiture1 = Voiture("Toyota", "Corolla", 2022, 150, "Essence", 5)

# Création d'une instance de Moto
moto1 = Moto("Honda", "YZF-R3", 2021, 42, "Essence", "Sport")

# Affichage des informations de la Voiture
print("Informations de la Voiture:")
voiture1.afficher_info()
print()

# Affichage des informations de la Moto
print("Informations de la Moto:")
moto1.afficher_info()
