'''Exercice 6 : Renommer et Supprimer des Fichiers
1. Écrivez un script qui renomme un fichier "phrases.txt" en "anciennes_phrases.txt".
2. Ensuite, supprimez le fichier "anciennes_phrases.txt".'''

import os

if __name__ == "__main__":

    old_name="phrases.txt"
    new_name="anciennes_phrases.txt"
    try:
        os.rename(old_name,new_name)
    except FileNotFoundError:
        print("fichier introuvable")
    except IOError:
        print("Erreur lors de ronnomage")
    else:
        print("DONE 1")

    try:
        os.remove(new_name)
    except FileNotFoundError:
        print("fichier introuvable")
    except IOError:
        print("Erreur lors de suppression")
    else:
        print("DONE 2")