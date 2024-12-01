#Exercice 10 : Fusionner des dictionnaires
#  Écrivez une fonction `fusionner_dicts(dict1, dict2)` qui prend deux dictionnaires en entrée et
#  retourne un dictionnaire fusionné. Si une clé est présente dans les deux dictionnaires, additionnez
#  leurs valeurs.


def fusionner_dicts(dict1, dict2):
    fusion = dict1 
    for cle, valeur in dict2.items():
        if cle in fusion:
            fusion[cle] += valeur  
        else:
            fusion[cle] = valeur  
    return fusion

dict1 = {"A": 1, "B": 2, "C": 3}
dict2 = {"B": 3, "C": 4, "D": 5}
print(fusionner_dicts(dict1, dict2))
