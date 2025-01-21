'''Exercice 5 : Multi-Exceptions
Écrivez une fonction `process_input(user_input)` qui tente de convertir `user_input` en entier et
d'effectuer une division par 10. Gérez les exceptions `ValueError` et `ZeroDivisionError` dans des
blocs `except` séparés, en affichant des messages d'erreur appropriés.'''

def process_input(user_input):
    try:
        number = int(user_input)
        result = 10 / number
        print(f"Le résultat de la division est : {result}")
    except ValueError:
        print("Erreur : L'entrée n'est pas un nombre valide.")
    except ZeroDivisionError:
        print("Erreur : Division par zéro impossible.")

# Exemples d'utilisation
process_input("5")    # Cas valide
process_input("abc")  # Cas invalide (ValueError)
process_input("0")    # Cas invalide (ZeroDivisionError)