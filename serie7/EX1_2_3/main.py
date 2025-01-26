
import conversion

# Exécuter les tests
if __name__ == "__main__":

    M=int(input("Entrer un montant en dollars $: "))
    try:
        print(f"le montant en DH est : \t {conversion.dollars_to_dirhams(M)}")
    except ValueError as e:
        print(e)

    D=int(input("Entrer une distance en m : "))
    try:
        print(f"la distance en Km est : \t {conversion.meters_to_kilometers(D)}")
    except ValueError as e:
        print(e)

#Exercice 2 : Utilisation des modules
#1. Le répertoire courant.
    import os
    cwd=os.getcwd()
    print(f"Le repertoire courant est :\t {cwd}")

#2. La date et l'heure actuelles.
    from datetime import datetime
    print(str(datetime.now()))

#3. La racine carrée d'un nombre donné par l'utilisateur.

    from math import sqrt
    a=int(input ('entrer un nombre a = '))
    print(f"Le racine carre de a est :  {sqrt(a)}")




   