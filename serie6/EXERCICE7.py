"""Exercice 7 : Journalisation des Exceptions
Utilisez le module `logging` pour créer une fonction `log_error(message)` qui enregistre les erreurs
dans un fichier `error.log`. Modifiez l'exercice 3 pour utiliser cette fonction pour enregistrer une
erreur si le fichier n'est pas trouvé."""

import logging

# Configuration du logging
logging.basicConfig(
    filename='error.log', 
    level=logging.ERROR, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(message):
    logging.error(message)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        error_message = f"Erreur : Le fichier '{filename}' n'a pas été trouvé."
        print(error_message)
        log_error(error_message)
    except IOError as e:
        error_message = f"Erreur d'entrée/sortie lors de la lecture du fichier '{filename}': {e}"
        print(error_message)
        log_error(error_message)
    except Exception as e:
        error_message = f"Une erreur inattendue s'est produite lors de la lecture du fichier '{filename}': {e}"
        print(error_message)
        log_error(error_message)

# Test de la fonction
read_file("tett.txt")