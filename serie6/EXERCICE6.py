'''Exercice 6 : Utilisation de `else` et `finally`
Modifiez l'exercice 1 pour inclure un bloc `else` qui imprime un message indiquant que la division
a été effectuée avec succès, et un bloc `finally` qui indique que la fonction est terminée, quel que
soit le résultat.'''

def safe_division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Erreur : Division par zéro impossible.")
        result = a / b
    except ZeroDivisionError as e:
        print(e)
    else:
        print(f"La division a été effectuée avec succès. Résultat : {result}")
        return result
    finally:
        print("La fonction est terminée.\n")

# Exemples d'utilisation
print("Test 1 : Division valide")
safe_division(10, 2)  # Cas valide

print("Test 2 : Division par zéro")
safe_division(10, 0)  # Cas invalide (division par zéro)
