#Exercice 4 : Dictionnaires
#Écrivez une fonction `compte_occurences(liste)` qui prend une liste de mots et retourne un dictionnaire où les clés sont les mots et les valeurs sont le nombre d'occurrences de chaque mot.

def compte_occurences(liste):
    occurence={}
    for mot in liste:
        if mot in occurence:
            occurence[mot]+=1
        else:
            occurence[mot]=1
    return occurence

liste3 = ["cat", "dog", "cat", "bird","cat","bird"]
print(compte_occurences(liste3)) 