'''Exercice 8 : Gestion des Erreurs
1. Écrivez un script qui tente d'ouvrir un fichier nommé "inexistant.txt" pour lecture.
2. Gérez l'exception qui pourrait survenir si le fichier n'existe pas en affichant un message d'erreur
approprié.'''

if __name__ == '__main__':
    try:
        with open("inexistant.txt", mode='r') as fichier:
            lignes= fichier.readlines
            print(lignes)
    except FileNotFoundError:
        print("Ce fichier n'existe pas ")
