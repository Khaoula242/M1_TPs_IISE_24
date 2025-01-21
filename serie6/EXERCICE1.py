'''Exercice 1 : Division par Zéro
Écrivez une fonction `safe_division(a, b)` qui prend deux arguments et renvoie le résultat de la
division de `a` par `b`. Si `b` est zéro, la fonction doit lever une exception `ZeroDivisionError` avec
un message approprié.'''

def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("Erreur : Division par zéro impossible.")
    return a / b

try:
    print(safe_division(10, 2))  # Cas valide
except ZeroDivisionError as e:
    print(e)

try:
    print(safe_division(10, 0))  # Cas invalide (division par zéro)
except ZeroDivisionError as e:
    print(e)


