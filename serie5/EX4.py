'''Exercice 4 : Traitement de Fichiers CSV
1. Créez un fichier CSV nommé "contacts.csv" avec les colonnes "Nom", "Âge", et "Ville".
2. Écrivez un script qui lit ce fichier et affiche les informations de chaque contact dans un format
lisible (ex. : "Nom : Alice, Âge : 30, Ville : Paris").'''

import csv

if __name__ == "__main__":
    agenda= [
           ["Nom", "Age","Ville"],
           ["layla", 23, "Agadir"],
           ["badr", 21, "Fes"]
    ]
    with open("contact.csv",mode="w", newline="") as file:
        E=csv.writer(file)
        E.writerows(agenda)
    
    with open("contact.csv", mode="r",newline="") as file:
        L=csv.reader(file)
        for i,ligne in enumerate(L):
            if i == 0:
                continue
            print( "Nom : {}, Âge : {}, Ville : {}".format(ligne[0], ligne[1], ligne[2]))

