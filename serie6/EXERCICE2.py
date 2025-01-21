'''Exercice 2 : Vérification de Type
Créez une fonction `convert_to_int(value)` qui tente de convertir `value` en entier. Si `value` n'est
pas convertible, la fonction doit lever une exception `ValueError` avec un message indiquant que la
conversion a échoué.'''

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("Conversion en entier échouée.")

if __name__ =='__main__':
    A=input("Entrer une valeur pour la conversion")
    convert_to_int(A)