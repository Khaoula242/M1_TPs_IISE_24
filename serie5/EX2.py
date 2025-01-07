'''Exercice 2 : Écriture dans un Fichier
1. Écrivez un script qui demande à l'utilisateur d'entrer trois phrases.
2. Enregistrez ces phrases dans un fichier nommé "phrases.txt", chaque phrase devant être sur une
nouvelle ligne'''

if __name__ == '__main__':
    list=[]
    for i in range(3):
        phrase=input('Entrer une phrase ')
        list.append(phrase+"\n")
    with open("phrases.txt", mode='w') as file:
        file.writelines(list)



