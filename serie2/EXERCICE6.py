class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)


# Exemple d'utilisation
# Création d'une instance de Rectangle
mon_rectangle = Rectangle(5, 10)

# Affichage de la surface et du périmètre
surface = mon_rectangle.calculer_surface()
perimetre = mon_rectangle.calculer_perimetre()

print("Surface : {}".format(surface))
print("Périmètre : {}".format(perimetre))
