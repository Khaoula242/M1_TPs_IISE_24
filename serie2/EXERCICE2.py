class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    
    def afficher_info(self):
        print("Marque : {}____ Modèle : {}____ Année : {}".format(self.marque, self.modele, self.annee))

# Exemple d'utilisation

voiture1 = Voiture("Toyota", "Corolla", 2020)
voiture2 = Voiture("Tesla", "Model S", 2022)
voiture3 = Voiture("Ford", "Mustang", 2018)
voiture1.afficher_info()