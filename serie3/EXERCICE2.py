class Personne():
    def __init__(self,__nom,__prenom,__age):
        self.__nom=__nom
        self.__prenom=__prenom
        self.__age=__age

    def getnom(self):
        return self.__nom
    def setnom(self, nom):
        self.__nom=nom
    def getprenom(self):
        return self.__prenom
    def setprenom(self,prenom):
        self.__prenom=prenom
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age=age


if __name__=="__main__":
    personne1=Personne("ali","charqawi",22)
    print("Nom :\t{}\nPrenom :{}\nAge :\t{}\n".format(personne1.getnom(),personne1.getprenom(),personne1.getage()))
    personne1.setage(24)  #changement de l'attribut age
    print("Nom :\t{}\nPrenom :{}\nAge :\t{}\n".format(personne1.getnom(),personne1.getprenom(),personne1.getage()))
