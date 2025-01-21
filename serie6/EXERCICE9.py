'''Exercice 9 : Gestion des Exceptions dans les Boucles
Créez une fonction `get_positive_integer()` qui demande à l'utilisateur de saisir un entier positif.
Utilisez une boucle pour continuer à demander jusqu'à ce qu'une saisie valide soit fournie. Gérez les
exceptions de conversion et vérifiez que l'entier est positif.'''


def get_positive_integer():
    while True:
        try:
            number = int(input("Entrez un entier positif : "))
            if number < 0:
                raise ValueError("L'entier doit être positif.")
            return number
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez réessayer.")

# Exemple d'utilisation
positive_integer = get_positive_integer()
print(f"Vous avez saisi : {positive_integer}")
