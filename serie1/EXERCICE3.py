#Exercice 3 : Ensembles
#Écrivez une fonction `intersection(ensemble1, ensemble2)` qui prend deux ensembles en entrée et retourne un nouvel ensemble contenant les éléments présents dans les deux ensembles


def intersection(ensemble1,ensemble2):
    ens=set()
    for element in ensemble1:
        if element in ensemble2:
            ens.add(element)
    return ens
ensemble1={1,8,9,6,4}
ensemble2={3,6,9,5,8}
print(intersection(ensemble1,ensemble2))