''''Exercice 7 : Copie et Déplacement de Fichiers
1. Créez un fichier texte nommé "journal.txt" et ajoutez quelques lignes de texte.
2. Écrivez un script qui copie ce fichier dans un nouveau fichier nommé "journal_copie.txt".
3. Déplacez "journal_copie.txt" dans un nouveau dossier nommé "archives".'''

import shutil
import os

if __name__ == "__main__":
    with open("journal.txt", mode="w") as fichier:
        fichier.write("bonjour \ntous le monde\ncomment allez-vous\n?  \n ")

    shutil.copy("journal.txt","journal_copie.txt")


    source = "journal_copie.txt"
    destination_dir = "archives"
    destination = os.path.join(destination_dir, "journal_copie.txt")

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    shutil.move(source,destination)