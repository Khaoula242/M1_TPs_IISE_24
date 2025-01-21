'''Exercice 4 : Exceptions Personnalisées
Créez une exception personnalisée `NegativeAgeError`. Écrivez une fonction `set_age(age)` qui
lève cette exception si l'âge est négatif. Testez la fonction dans un bloc `try` et gérez l'exception en
imprimant un message approprié.'''


class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("L'âge ne peut pas être négatif.")

try:
    set_age(-5)
except NegativeAgeError as e:
    print(f"Erreur : {e}")
