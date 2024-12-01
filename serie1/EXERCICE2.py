#Exercice 2 : Tuples
#Écrivez une fonction `max_tuple(t)` qui prend un tuple de nombres et retourne le plus grand nombre dans le tuple.


def max_tuple(t):
    max=0
    for element in t:
        if element>max:
            max=element
    return max

tuple1=(1,2,4,6,10)
print("le max dans tuple1 est :", max_tuple(tuple1))