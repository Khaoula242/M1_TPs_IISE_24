#Exercice 6 : Fonctions anonymes
#Utilisez une fonction lambda pour créer une fonction `carre` qui prend un nombre en entrée et retourne son carré

carre= lambda x : x**2
print(carre(3))

print((lambda x: x**2)(5))