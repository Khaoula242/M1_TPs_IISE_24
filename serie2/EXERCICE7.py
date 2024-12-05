class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    ######Definition de methode speciale __str__
    def __str__(self):
        return "'{}' par '{}' Publié en {}\n".format(self.titre,self.auteur,self.annee_publication)
   
class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print("Livre ajouté : {}".format(livre))

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Livres dans la bibliothèque :\n")
            for livre in self.livres:
                print("\t- {}".format(livre))

# Exemple d'utilisation
bibliotheque = Bibliotheque()
livre1 = Livre("La boîte à merveilles", "Ahmed Sefrioui", 1954)
livre2 = Livre("Les Misérables", "Victor Hugo", 1862)

bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.afficher_livres()
