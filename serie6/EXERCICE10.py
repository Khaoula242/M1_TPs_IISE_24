'''Exercice 10 : Combinez Tout
Écrivez un programme qui demande à l'utilisateur de saisir un fichier, puis un entier. Utilisez les
concepts de gestion des exceptions pour garantir que le fichier est lu avec succès et que l'entier est
valide. Gérer toutes les exceptions appropriées et afficher des messages utiles.'''

def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            print("Contenu du fichier :")
            print(contenu)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'a pas été trouvé.")
    except IOError:
        print(f"Erreur : Impossible de lire le fichier '{nom_fichier}'.")
    except Exception :
        print("Error!!!")

def saisir_entier():
    while True:
        try:
            entier = int(input("Veuillez saisir un entier : "))
            return entier
        except ValueError:
            print("Erreur : Vous devez saisir un entier valide. Veuillez réessayer.")
        except Exception :
            print("Error!!!")

def main():
    # Demander à l'utilisateur de saisir un fichier
    nom_fichier = input("Veuillez saisir le nom du fichier à lire : ")
    lire_fichier(nom_fichier)

    # Demander à l'utilisateur de saisir un entier
    entier = saisir_entier()
    print(f"Vous avez saisi l'entier : {entier}")

if __name__ == "__main__":
    main()