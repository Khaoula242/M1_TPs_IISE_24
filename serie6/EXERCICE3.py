'''Exercice 3 : Lecture de Fichier
Écrivez une fonction `read_file(filename)` qui tente d'ouvrir et de lire un fichier. Si le fichier
n'existe pas, la fonction doit gérer l'exception `FileNotFoundError` et imprimer un message d'erreur.
Utilisez également un bloc `finally` pour garantir que le fichier est fermé.'''


def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'a pas été trouvé.")
    else:
        print(content)
    finally:
        # S'assurer que le fichier est fermé, même si une exception est levée
        if 'file' in locals():
            file.close() #Cette instruction sans condition 'if' déclenche une erreur si le fichier n'a pas été ouvert
            print("Le fichier a été fermé.")

# Exemple d'utilisation
read_file("testt.txt")

