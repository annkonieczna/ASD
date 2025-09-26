#Las- graf 
#drzewa- wierzchołki 
#krawędzie - systemy korzeniowe 


#Badamy system korzeni: 

# 1. Wybieramy k drzew i wszczepiamy im k gatunków grzyba numerowanych od 0 do k-1 
# W 1 s grzyb przechodzi na wszystkich sąsiadów 
# jeśli 2 lub więcej gatunków grzyba dociera do danego drzewa w tym samym czasie to wygrywa ten z mniejszym indeksem 

#Algorytm ma policzyć ile drzew zostanie zakażonych przez grzyba o indeksie d 

#Graf ma postać adj list 
#Tablica T zawiera numery drzew, którym wszczepiono grzyby,

from collections import deque 

def Pandora(G,T,d): 

    n = len(G) # liczba drzew 

    k = len(T) # liczba grzybów 
    #Tablica drzew, którym wszczepiono grzyb. T[i] - numer drzewa, któremu wszczepiono i-ty grzyb 


    distance = [-1*k]*n #tablica dystansów  
    mushroom = [-1]*n # tablica jaki grzyb doszedł do jakiego drzewa 

    q = deque()

    #inicjalizujemy grzyby

    for i in range(k): 
        #grzyb i startuje z drzewa  
        tree = T[i]
        distance[tree][i] = 0
        mushroom[tree] = i
        deque((distance[tree][i],tree,i))


    while q: 
        dist, tree, mush = q.popleft

        for next_tree in G[tree]: 

            if distance[next_tree] == -1: 
                distance[next_tree] = dist + 1 
                mushroom[next_tree] = mush
                q.append((distance[next_tree][mush],next_tree,i))
            else: 
                if distance[next_tree][mush] == dist + 1: 
                    if mushroom[next_tree] > mush: 
                        mushroom[next_tree] = mush 
                        q.append((distance[next_tree][mush],next_tree,mush))
    counter = 0 
    for elements in mushroom: 
        if elements == d: 
            counter += 1 


    return counter 






    
