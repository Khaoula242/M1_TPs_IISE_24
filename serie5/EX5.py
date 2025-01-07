"""
Exercice 5 : Écriture et Lecture de Fichiers JSON
1. Créez un dictionnaire Python contenant des informations sur trois étudiants (nom, âge, et note).
2. Enregistrez ce dictionnaire dans un fichier JSON nommé "etudiants.json".
3. Écrivez un script qui lit ce fichier JSON et affiche les informations de chaque étudiant."""

import json

if __name__  == '__main__':
    Dict={"Etudiant_1":{"nom":"jamila","age":22, "note":15},
          "Etudiant_2":{"nom":"said","age":23,"note":15},
          "Etudiant_3":{"nom":"karima","age":23, "note":16}}


    with open("etudiants.json", mode='w') as fichier:
        json.dump(Dict,fichier, indent=4)

    with open("etudiants.json", mode="r") as file:
        donnee=json.load(file)
        for k in donnee.keys():
            print(k+" :\t")
            for c,val in donnee[k].items():
                print(c,val)