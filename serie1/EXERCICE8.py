#Exercice 8 : Fonctions variadiques
#Écrivez une fonction `somme_varargs(*args)` qui prend un nombre variable d'arguments et retourne la somme de ces arguments.

def somme_varargs(*args):
    somme=0
    for nmbr in args:
        somme+=nmbr
    return somme   
tuple3=(1,3,4,9)
print(somme_varargs(*tuple3))
