#Exercice 5 : Fonction récursive
#Écrivez une fonction récursive `factorielle(n)` qui retourne la factorielle d'un nombre entier `n`.

def factorielle(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorielle(n-1)

print(factorielle(5))
