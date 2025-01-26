import pandas as pd

def main():
    """
    Analyse un fichier CSV contenant des informations sur des employés.
    1. Affiche les cinq premières lignes du fichier.
    2. Calcule et affiche la moyenne d'un champ numérique (par exemple, l'âge des employés).
    """
    # Étape 1 : Charger le fichier CSV
    try:
        data = pd.read_csv("EX5/employees.csv")
    except FileNotFoundError:
        print("Erreur : Le fichier 'employees.csv' est introuvable.")
        return
    except Exception as e:
        print(f"Une erreur s'est produite lors du chargement du fichier : {e}")
        return

    # Étape 2 : Afficher les cinq premières lignes du DataFrame
    print("Les cinq premières lignes du fichier :")
    print(data.head())

    # Étape 3 : Calculer et afficher la moyenne d'un champ numérique (par exemple, l'âge)
    if "Age" in data.columns:  # Vérifie si la colonne "Age" existe
        mean_age = data["Age"].mean()
        print(f"\nLa moyenne de l'âge des employés est : {mean_age:.2f}")
    else:
        print("\nErreur : Le champ 'Age' n'existe pas dans le fichier.")

if __name__ == "__main__":
    main()
