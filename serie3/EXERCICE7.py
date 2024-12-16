from abc import ABC,abstractmethod

##Création de classe abstraite "Vehicule"
class Vehicule(ABC):
    @abstractmethod
    def deplacer():
        pass
    
##Création de sous-classe "Voiture"
class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture démarre et roule sur l'autoroute à 100 km/h.")


##Création de sous-classe "Bicyclette"
class Bicyclette(Vehicule):
    def deplacer(self):
        print("La bicyclette avance à 20 km/h grâce à l'effort du cycliste.")


if __name__ == "__main__":
    voiture = Voiture()
    bicyclette = Bicyclette()

    voiture.deplacer()      
    bicyclette.deplacer()  
