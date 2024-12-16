class Produit():
    def __init__(self,nom,prix):
        self.nom=nom
        self.prix=prix
        

class Commande():
    def __init__(self,produit,Q):
        self.produit=produit
        self.Q=Q   # Quantité commandée

class Panier():
    def __init__(self):
        self.list_commande=[]    # Liste des commandes

    def ajouter_commande(self,Newcommande):
        self.list_commande.append(Newcommande)
        
    def calcul_Total(self):
        total=0
        for element in self.list_commande:
            total+=element.Q*element.produit.prix
        return total
    



if __name__ == "__main__":
    # Création de produits
    produit1 = Produit("Pomme", 20)  
    produit2 = Produit("Banane", 15) 

    # Création de commandes
    commande1 = Commande(produit1, 5)  # 5 pommes
    commande2 = Commande(produit2, 10)  # 10 bananes

    # Création d'un panier
    panier = Panier()

    # Ajout des commandes au panier
    panier.ajouter_commande(commande1)
    panier.ajouter_commande(commande2)

    # Affichage du panier et du total
    print("le total de ce panier est : {}".format(panier.calcul_Total()))

