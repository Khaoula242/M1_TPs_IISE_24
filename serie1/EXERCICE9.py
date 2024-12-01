#Exercice 9 : Analyser un texte
#Écrivez une fonction `analyse_texte(texte)` qui prend une chaîne de caractères, compte le nombre de mots et retourne un dictionnaire avec le nombre de mots et le nombre de caractères.

def analyse_texte(texte):
    Dict={"mots":1,"caracteres":0}
    if len(texte)==0:
        return "chaine vide"
    else:
        for i in texte:
            if i == ' ':
                Dict["mots"]+=1
            else:
                Dict["caracteres"]+=1
    return Dict

print(analyse_texte("It is never too late to be what you might have been"))


########################version2###################################
###################################################################
def analyse_texte2(texte):
    D={"nombre de mots":0 ,"nombre de caractères":0} 
    list=texte.split()
    nbr_mots=len(list)
    nbr_car=len(texte)
    D["nombre de mots"]=nbr_mots
    D["nombre de caractères"]=nbr_car-(nbr_mots-1)
    return D 
print(analyse_texte2(""))