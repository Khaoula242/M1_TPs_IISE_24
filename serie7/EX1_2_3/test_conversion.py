"""Exercice 3 : Écriture de tests unitaires
Écrivez des tests unitaires pour le module "conversion.py" que vous avez créé dans l'exercice 1.
1. Créez un fichier "test_conversion.py".
2. Utilisez "unittest" pour tester toutes les fonctions de votre module.
3. Vérifiez que les fonctions retournent les résultats attendus."""


import conversion as c
import unittest

class TestConversion(unittest.TestCase):
    def test_dollars_to_dirhams_positive(self):
        self.assertEqual(c.dollars_to_dirhams(1200), (1200 * 10.5))

    def test_dollars_to_dirhams_negative(self):
        with self.assertRaises(ValueError):
            c.dollars_to_dirhams(-12)

# Exécuter les tests
if __name__ == "__main__":
    unittest.main()



   