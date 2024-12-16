import math
from abc import ABC, abstractmethod


##Création de classe abstraite "Forme"
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass
    
class Circle(Forme): 
    def __init__(self,r):
        self.r=r

    def calculer_surface(self):
        return math.pi*(self.r**2)
    
class Rectangle(Forme):
    def __init__(self,Lar,Lon):
        self.Lar=Lar
        self.Lon=Lon

    def calculer_surface(self):
        return self.Lon*self.Lar
    
## methode pour afficher la surface de chaque forme
def afficher_surface(Formes):
    i=1
    for forme in Formes:
        print("la surface de forme {} est: {:.2f}".format(i,forme.calculer_surface()))
        i+=1

if __name__ == "__main__":
    cercle = Circle(3)
    rectangle = Rectangle(4, 6)
    formes = [cercle, rectangle]

    afficher_surface(formes)


    
        

        
