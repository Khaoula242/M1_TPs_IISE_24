import math
from abc import ABC,abstractmethod

##Création de classe abstraite "Forme"
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

##Création de sous-classe "Cercle"
class Cercle(Forme):
    def __init__(self,Rayon):
        self.Rayon=Rayon

    def calculer_surface(self):
        return math.pi*(self.Rayon ** 2)
    
##Création de sous-classe "Rectangle"
class Rectangle(Forme):
    def __init__(self,La,lo):
        self.La=La
        self.Lo=lo
    def calculer_surface(self):
        return self.La*self.Lo
    
if __name__=="__main__":
    Cer1=Cercle(5)
    Rec1=Rectangle(4,20)

    print("la surface de circle est {:.2f}:".format(Cer1.calculer_surface()))
    print("la surface de rectangle est :{} ".format(Rec1.calculer_surface()))
        
       
