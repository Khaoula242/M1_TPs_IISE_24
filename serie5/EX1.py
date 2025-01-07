

if __name__ == '__main__':
    list=["   La Métamorphose      \n","Un matin, en s’éveillant d’un rêve agité, Gregor Samsa se retrouva,\n",
          " dans son lit, métamorphosé en un monstrueux insecte.\n",
          " Il était couché sur le dos, dur comme une carapace,\n",
          " et, en levant un peu la tête, il voyait son ventre bombé, brun,\n",
          " séparé par des arceaux rigides, sur lequel la couverture,\n",
          " prête à glisser tout à fait, ne tenait plus qu’à grand-peine.\n",
          " Ses nombreuses pattes, d’une pitoyable minceur, comparées à la taille\n",
          " normale de ses jambes, s’agitaient désespérément devant ses yeux.\n"]
   
    with open("exemple.txt", mode="w") as fichier:
        fichier.writelines(list)
    
    with open("exemple.txt", mode="r") as fichier:
        ligne = fichier.readline()
        i=1
        while ligne:
            print(str(i) +". "+ligne)
            i=i+1
            ligne = fichier.readline()
