'''Exercice 8 : Tests Unitaires pour les Exceptions
Écrivez des tests unitaires pour vérifier que les exceptions sont levées correctement dans les
fonctions que vous avez créées dans les exercices précédents. Utilisez le module `unittest` pour
cela.'''

import unittest


def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division par zéro.")
    

class TestExceptions(unittest.TestCase):
    def test_safe_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10, 0)

# Exécuter les tests
if __name__ == "__main__":
    unittest.main() 



