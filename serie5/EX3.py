'''Exercice 3 : Ajout à un Fichier
1. Modifiez le script précédent pour qu'il demande à l'utilisateur s'il souhaite ajouter d'autres phrases
à "phrases.txt".
2. Si l'utilisateur répond "oui", permettez-lui d'ajouter autant de phrases qu'il le souhaite, en
s'assurant que ces phrases sont ajoutées à la fin du fichier.'''

if __name__ == '__main__':
    phrases=[]
    for i in range(3):
        phrase=input('Entrer une phrase: \t')
        phrases.append(phrase+"\n")
    while True:
        a= input("Vous souhaitez ajouter d'autres phrases .oui/non\t")
        if a == "oui":
            phrase=input('Entrer votre contenu\t: ')
            phrases.append(phrase+"\n")
        else:
            break    
    with open("phrases1.txt", mode='a') as file:
        file.writelines(phrases)




