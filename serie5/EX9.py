'''Exercice 9 : Statistiques de Fichier
1. Écrivez un script qui lit un fichier texte et calcule :
 - Le nombre total de lignes.
 - Le nombre total de mots.
 - Le nombre total de caractères.
2. Affichez ces statistiques à l'utilisateur'''


if __name__ == '__main__':

    try:
        with open("exemple.txt", mode='r') as fichier:
            texte = fichier.readlines() #texte est une liste de ligne
    except FileNotFoundError:
        print("le fichier n'existe pas")
    else:
        nombreLigne= len(texte)
        nombreMots = 0
        for ligne in texte:
            nombreMots += len(ligne.split(' '))
        
        nombreC=0
        for ligne in texte:
            nombreC += len(ligne)

        print("Le nombre total de lignes :{}".format(nombreLigne))
        print("Le nombre total de Mots :{}".format(nombreMots))      
        print("Le nombre total de caractères :{}".format(nombreC))