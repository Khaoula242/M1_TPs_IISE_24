#Exercice 7 : Fonctions avec des arguments par défaut
#Écrivez une fonction `salutation(nom, message="Bonjour")` qui affiche un message de salutation. Le message par défaut doit être "Bonjour".

def salutation(nom,message="Bonjour"):
    return message+' '+nom
print(salutation("Mark"))
print(salutation("Mark","salut"))
