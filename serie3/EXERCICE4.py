class Produit():
    # Méthode d'initialisation pour définir les attributs privés nom et prix
    def __init__(self, __nom, __prix):
        self.__nom = __nom
        self.__prix = __prix

    # Propriété pour accéder au nom
    @property
    def nom(self):
        return self.__nom
    
    # Setter pour modifier le nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    # Méthode privée pour obtenir le prix
    def __getprix(self):
        return self.__prix

    # Méthode privée pour définir le prix
    def __setprix(self, prix):
        # Vérifie que le prix est supérieur à 0 avant de l'attribuer
        if prix > 0:
            self.__prix = prix
        else:
            print("Le prix doit être supérieur à 0")

    # Utilisation de property pour l'encapsulation de l'attribut prix
    prix = property(__getprix, __setprix)

    # Méthode pour calculer une remise si le prix dépasse un certain seuil
    def Calcul_remise(self, pourcentage, seuil):
        if self.__prix > seuil:
            # Applique une remise en fonction du pourcentage
            self.__prix -= self.__prix * pourcentage / 100
        return self.__prix


# Exemple d'utilisation
if __name__ == "__main__":
    # Création de deux objets de la classe Produit
    produit1 = Produit("Ordinateur", 4000)
    produit2 = Produit("Clavier", 80)

    # Affichage du prix avant remise pour le premier produit
    print("Prix avant remise : {:.2f} ".format(produit1.prix)) 
    # Application d'une remise et affichage du prix après remise
    print("Prix après remise : {:.2f} ".format(produit1.Calcul_remise(10, 2000)))
